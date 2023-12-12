from src.function import Function
from src.dataFile import DataFile

def generateLatex(dataFile: DataFile) -> str:
    latexOutput =  f"\section{{{dataFile.getFileName()}}}\n\n"

    # Explain the file if there is a description
    if dataFile.hasDescription():
        latexOutput += f"{dataFile.getDescription()}\n\n"
    
    # Populate functions
    for function in dataFile.getFunctions():
        latexFunction = generateLatexFunction(function, dataFile.fileName)
        latexOutput += f"{latexFunction}\n\n"

    return latexOutput

def generateLatexFunction(function: Function, filename: str) -> str:
    dec1, dec2 = splitAtLength(f"{filename}.{function.getFonctionDec()}")

    if dec2 == "":
        latexOutput = f"\\begin{{func}}{{{dec1}}}\n"
    else:
        latexOutput = f"\\begin{{funcsplit}}{{{dec1}}}{{{dec2}}}\n"

    if function.description:
        latexOutput += f"    \\item {function.description}\n"

    if function.parameters:
        for param_name, param_description in function.parameters:
            latexOutput += f"    \\item \\param{{{param_name}}}{{{param_description}}}\n"
    
    if function.interruptions:
        for interruption_name, int_description in function.interruptions:
            latexOutput += f"    \\item \\inter{{{interruption_name}}}{{{int_description}}}\n"

    if function.returns:
        for ret_description in function.returns:
            latexOutput += f"    \\item \\ret{{{ret_description}}}\n"

    if function.urls:
        for url in function.urls:
            latexOutput += f"    \\item \\url{{{url}}}\n"

    if function.enums:
        for enum_name, enum_description in function.enums:
            latexOutput += f"    \\item \\enum{{{enum_name}}}{{{enum_description}}}\n"

    if dec2 == "":
        latexOutput += "\\end{funcsplit}\n"
    else:
        latexOutput += "\\end{func}\n"
    return latexOutput

def generateLatexMain(files: list[DataFile]) -> str:
    latexOutput =  "\\documentClass{article}\n\n"
    latexOutput += "\\input{packages.tex}\n\n"
    latexOutput += "\\begin{document}\n\n"

    for file in files:
        #print(file)
        fileName = file.getFileName()
        latexOutput += f"\input{{files/{fileName}}} \n\n"

    latexOutput += "\\end{document}\n\n"

    return latexOutput


def splitAtLength(string: str, maxlen: int =100) -> tuple[str, str]:
    words = string.split(', ')
    part1 = []
    part2 = []
    current_length = 0
    on_part2 = False

    for word in words:
        # Check if adding the current word exceeds the maximum length
        if current_length + len(word) + 1 <= maxlen and not on_part2:
            # Add the word and the comma to the result
            part1.append(word)
            current_length += len(word) + 1
        else:
            on_part2 = True
            # Add the word at the part2
            part2.append(word)

    # Join the result list into a string using ', ' as the separator
    formatted_part1 = ', '.join(part1)
    if len(part1) > 1 and len(part2) > 0:
        formatted_part1 += ","
    formatted_part2 = ', '.join(part2)

    return formatted_part1, formatted_part2
