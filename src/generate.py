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

    latexOutput += "\\end{func}\n"
    return latexOutput