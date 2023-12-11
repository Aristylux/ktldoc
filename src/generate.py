from .function import Function

def generateLatex(function: Function):
    latex_output = f"\\begin{{func}}{{{function.functionName}}}\n"

    if function.description:
        latex_output += f"    \\item {function.description}\n"

    if function.parameters:
        for param_name, param_description in function.parameters:
            latex_output += f"    \\item \\param{{{param_name}}}{{{param_description}}}\n"
    
    if function.interruptions:
        for interruption_name, int_description in function.interruptions:
            latex_output += f"    \\item \\inter{{{interruption_name}}}{{{int_description}}}\n"

    if function.returns:
        for ret_description in function.returns:
            latex_output += f"    \\item \\ret{{{ret_description}}}\n"

    latex_output += "\\end{func}\n"
    print(latex_output)