from src.extractors.extractorInterface import ExtractorInterface

from src.dataFile import DataFile

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