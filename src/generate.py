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
    latexOutput = f"\\begin{{func}}{{{filename}.{function.getFonctionDec()}}}\n"

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