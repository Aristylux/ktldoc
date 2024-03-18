from src.dataFile import RawData
from src.function import Function
from src.extractors.extractorInterface import ExtractorInterface

from src.dataFile import DataFile

import re

class PythonExtractor(ExtractorInterface):

    def extract(self, filePath: str, datafile: DataFile):
        with open(filePath, 'r') as file:

            maybe_comment = False
            in_comment = False
            current_comment = ""

            current_function = ""

            format_function = False

            for line in file:
                formLine = line.strip()

                if formLine.startswith('# ') and not maybe_comment:
                    maybe_comment = True
                    current_comment = formLine + "\n"
                elif formLine == "":
                    maybe_comment = False
                    current_comment = "" # Clean comment
                elif formLine.startswith('# @') and maybe_comment:
                    in_comment = True
                    current_comment += formLine + "\n"

                elif formLine.startswith('# ') and maybe_comment:
                    current_comment += formLine + "\n"

                # End of the comment, check the function ||| add '@' for async function?
                elif not formLine.startswith('# ') and in_comment and not formLine.startswith('@'):
                    #print(current_comment)
                    in_comment = False
                    format_function = True
                    current_function = formLine
                
                if format_function:
                    datafile.addRawData(current_comment, current_function)
                    current_comment = ""
                    current_function = ""
                    format_function = False

   

    def extractFunction(self, rawData: RawData, data: DataFile) -> Function:
        # print("Extract function")
        function = Function()

        # Extract function description
        function = self.__extractDescription__(rawData.comment)

        # Extract function declaration
        self.__extractDeclaration__(rawData.function, function)



        return function
    

    # @note: partialy generic
    def __extractDescription__(self, comment: str) -> Function:
        # print("Extract Description")
        # print(comment)
        # print("--------")

        function = Function()
        extracted_comment = ""

        lines = comment.split('\n')
        for line in lines:
            # General
            line = re.sub(r'\s+', ' ', line)       # Replace multiple spaces with a single space
            
            # Specific to .py
            line = line.lstrip('#').lstrip()

            # General ---

            # Param line
            if re.match(r'\s*@param', line):
                function.addParameter(self.extractParam(line.strip()))
            # Return line
            elif re.match(r'\s*@return', line):
                function.addReturn(self.extractReturn(line.strip()))
            # Note line
            elif re.match(r'\s*@note', line):
                function.addNote(self.extractReturn(line.strip()))
            # Empty line
            elif re.match(r'\s*\*', line):
                continue
            else:
                extracted_comment += line.strip() + ' '

        extracted_comment = self.formatString(extracted_comment)
        function.addDescription(extracted_comment)
        return function

    # Can be a general function
    def __extractDeclaration__(self, functionDeclaration: str, function: Function):
        print("Extract Declaration")

        # Extract the function name
        functionName = self.getFunctionName(functionDeclaration)

        # Extract and format parameters
        parameters = self.getParameters(functionDeclaration)

        print(f"\nfunction: {functionDeclaration}")
        print(f"--{functionName}({parameters})\n")

        # Format the result
        function.addFunctionName(functionName)
        function.addFunctionParameters(parameters)

    # Only pattern change from .kt
    def getFunctionName(self, functionDeclaration: str) -> str:
        print(f"Function declaration: {functionDeclaration}")
        functionNameMatch = re.search(r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', functionDeclaration)
        if functionNameMatch:
            return functionNameMatch.group(1)
        else:
            return "Invalid function declaration"
    
    # Same as extract.py
    def getParameters(self, functionDeclaration: str) -> list[str]:
        formatFun = functionDeclaration.replace(" ", "")
        parameters = []

        # Define a regular expression pattern to match the content inside the first pair of parentheses
        pattern = r'\((.*?)\)'

        # Use re.search to find the first match in the input string
        match = re.search(pattern, formatFun)

        # Check if there is a match and return the captured content group
        if match:
            # Split the string at the first occurrence of ':'
            parts = match.group(1).split(',')
            for part in parts:
                if ':' in part:
                    param = part.split(":")
                    # Check if there is at least one part
                    if len(param) > 0:
                        parameters.append(param[0])

        return parameters

    # -------- From extract.py -----------
    # Can be general function

    def extractParam(self, line: str) -> tuple[str, str]:
        parts = line.split()
        if len(parts) > 1:
            param_name = parts[1]
            description = ' '.join(parts[2:])
            # description = formatString(description)
            description = self.formatString(description)
            return param_name, description
        else:
            return "", ""
    

    # def extractReturn(line: str) -> str:
    def extractReturn(self, line: str) -> str:
        # return formatString(' '.join(line.split()[1:]))
        return self.formatString(' '.join(line.split()[1:]))
    
    # def formatString(string: str) -> str:
    def formatString(self, string: str) -> str:
        # Capitalize the first letter
        formatted_string = string.capitalize()

        # Remove trailing spaces
        formatted_string = formatted_string.rstrip()

        # Add a '.' at the end if not present
        if not formatted_string.endswith('.'):
            formatted_string += '.'

        # Replace every '\' with '\\'
        formatted_string = formatted_string.replace('\\', '\\\\')

        # Define a regular expression pattern to match "`CODE`"
        pattern = r'`([^`]+)`'

        # Use re.sub to replace matches with the desired format
        formatted_string = re.sub(pattern, r'\\code{\1}', formatted_string)

        return formatted_string