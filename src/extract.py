import os
import re

def extractData(file_path: str):

    # Get the filename without extension
    filename = os.path.splitext(os.path.basename(file_path))[0]

    with open(file_path, 'r') as file:
        format_function = False
        inside_comment = False
        check_function = False
        current_comment = ""
        inside_function = False
        current_function = ""

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
                # in one line
                if re.search(r'\bfun\b', line) and (re.search(r'[\s]*{', line) or re.search(r'{', line)): #and line.strip().endswith('{'):
                    current_function = line.strip()
                    format_function = True

                elif re.search(r'\bfun\b', line):
                    current_function = line.strip()
                    inside_function = True
                
                elif inside_function and (re.search(r'[\s]*{', line) or re.search(r'{', line)):
                    current_function += line.strip()
                    inside_function = False
                    format_function = True

                elif inside_function:
                    current_function += line.strip()
            
            if format_function:
                print(f"Extract Comment:\n{current_comment}")
                print(f"Generate Function:\n{current_function}")
                #extracted_comment, params, interruptions, returns, notes = extract_comment(current_comment)
                #generate_latex(file_name + "." + format_kotlin_function(current_function), extracted_comment, params, interruptions, returns)
                format_function = False
                print("------------------")
                current_function = ""