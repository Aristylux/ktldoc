import os
import re

from src.function import Function
from src.dataFile import DataFile, FileType, RawData

from src.extractors.kotlin import KotlinExtractor
from src.extractors.python import PythonExtractor



def extractData(file_path: str) -> DataFile:
    datafile = DataFile()

    # Get the filename without extension
    namename, extension = os.path.splitext(os.path.basename(file_path))

    datafile.setFilename(namename)
    datafile.setExtension(extension)

    if datafile.getExtension() == ".kt":
        extractor = KotlinExtractor()
    elif datafile.getExtension() == ".py":
        extractor = PythonExtractor()
    else:
        extractor = None

    if extractor is not None:
        extractor.extract(file_path, datafile)

    return datafile
    
# ---

def extractFunction(rawData: RawData, data: DataFile) -> Function:
    function = extractComment(rawData.comment)

    if data.getType() == FileType.ENUM:
        extractEnum(rawData.function, function)
    else:
        extractDeclaration(rawData.function, function)

    return function


def extractParam(line: str) -> tuple[str, str]:
    parts = line.split()
    if len(parts) > 1:
        param_name = parts[1]
        description = ' '.join(parts[2:])
        description = formatString(description)
        return param_name, description
    else:
        return "", ""
    

def extractReturn(line: str) -> str:
    return formatString(' '.join(line.split()[1:]))

def extractComment(comment: str) -> Function:
    function = Function()
    extracted_comment = ""

    lines = comment.split('\n')
    for line in lines:
        
        line = re.sub(r'^\s*\*\s*', '', line)  # Remove leading spaces, tabs, and asterisks
        line = re.sub(r'\s+', ' ', line)       # Replace multiple spaces with a single space
        
        if re.match(r'\s*@param', line):
            function.addParameter(extractParam(line.strip()))
        elif re.match(r'\s*@interruption', line):
            function.addInterruption(extractParam(line.strip()))
        elif re.match(r'\s*@return', line):
            function.addReturn(extractReturn(line.strip()))
        elif re.match(r'\s*@note', line):
            function.addNote(extractReturn(line.strip()))
        elif re.match(r'\s*@url', line):
            function.addUrl(extractReturn(line.strip()))
        elif re.match(r'\s*@enum', line):
            function.addEnum(extractParam(line.strip()))
        elif re.match(r'\s*\*', line):
            continue
        else:
            extracted_comment += line.strip() + ' '
    extracted_comment = formatString(extracted_comment)
    function.addDescription(extracted_comment)
    return function

def extractDeclaration(functionDeclaration: str, function: Function) -> None:
    # Extract the function name
    functionName = getFunctionName(functionDeclaration)

    # Extract and format parameters
    parameters = getParameters(functionDeclaration)

    # print(f"\nfunction: {functionDeclaration}")
    # print(f"--{functionName}({parameters})\n")

    # Format the result
    function.addFunctionName(functionName)
    function.addFunctionParameters(parameters)

def getFunctionName(functionDeclaration: str) -> str:
    functionNameMatch = re.search(r'\bfun\s+([\w.]+)\s*\(', functionDeclaration)
    if functionNameMatch:
        return functionNameMatch.group(1)
    else:
        return "Invalid function declaration"

def extractEnum(enum: str, function: Function) -> None:
    enumName = getEnumName(enum)
    function.addFunctionName(enumName)

def getEnumName(enumDeclaration: str) -> str:
    # Define a regular expression pattern to match "enum class NAME" or "enum class NAME {"
    pattern = r'enum\s+class\s+(\w+)\s*\{?'

    # Use re.search to find the match in the input string
    EnumNamematch = re.search(pattern, enumDeclaration)

    # Check if there is a match and return the captured name group
    if EnumNamematch:
        return EnumNamematch.group(1)
    else:
        return "Invald enum declaration"

def getParameters(functionDeclaration: str) -> list[str]:
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

def formatString(string: str) -> str:
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
