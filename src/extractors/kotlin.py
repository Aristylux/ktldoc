from src.extractors.extractorInterface import ExtractorInterface

import re

from src.dataFile import DataFile, FileType

class KotlinExtractor(ExtractorInterface):

    def extract(self, filePath: str, datafile: DataFile):
        with open(filePath, 'r') as file:
            format_function = False
            inside_comment = False
            check_function = False
            inside_function = False
            current_comment = ""
            current_function = ""

            # Read line by line
            for line in file:
                if line.lstrip().startswith('/**') and not re.search('[a-zA-Z]', line):
                    inside_comment = True
                    current_comment = ""
                
                elif inside_comment and line.lstrip().startswith('*/'):
                    inside_comment = False
                    check_function = True

                elif inside_comment:
                    current_comment += line

                elif check_function:
                    # FUNCTION In one line
                    if re.search(r'\bfun\b', line) and (re.search(r'[\s]*{', line) or re.search(r'{', line)): #and line.strip().endswith('{'):
                        current_function = line.strip()
                        format_function = True
                    # FUNCTION More than one line
                    elif re.search(r'\bfun\b', line):
                        current_function = line.strip()
                        inside_function = True
                    # ENUM
                    elif re.search(r'\benum class\b', line):
                        current_function = line.strip()
                        datafile.setType(FileType.ENUM)
                        format_function = True
                    
                    elif inside_function and (re.search(r'[\s]*{', line) or re.search(r'{', line)):
                        current_function += line.strip()
                        inside_function = False
                        format_function = True

                    elif inside_function:
                        current_function += line.strip()
                
                if format_function:
                    datafile.addRawData(current_comment, current_function)
                    format_function = False
                    current_function = ""
                    current_comment = ""