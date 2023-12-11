class Function:
    def __init__(self) -> None:
        self.functionName = ""
        self.functionParameters = ""
        self.description = ""
        self.parameters = []
        self.interruptions = []
        self.returns = []
        self.notes = []
        pass

    def addFunctionName(self, functionName: str):
        self.functionName = functionName

    def addFunctionParameters(self, parameters: list[str]):
        self.functionParameters = parameters

    def addDescription(self, description: str):
        self.description = description

    def addParameter(self, param : tuple[str, str]):
        self.parameters.append(param)

    def addInterruption(self, interruption: tuple[str, str]):
        self.interruptions.append(interruption)

    def addReturn(self, returnDesc: str):
        self.returns.append(returnDesc)

    def addNote(self, noteDesc: str):
        self.notes.append(noteDesc)

    def getFonctionDec(self):
        nbrParams = len(self.functionParameters)
        params = "("
        for paramIndex in range(nbrParams - 1):
            params += f"{self.functionParameters[paramIndex]}, "
        params += f"{self.functionParameters[nbrParams - 1]})"
        return f"{self.functionName}{params}"

    def __str__(self) -> str:

        param = "[\n"
        for paramName, paramDesc in self.parameters:
            param += f"\t('{paramName}' - '{paramDesc}')\n"
        param += "                  ]"

        return f"""Function:{self.functionName}({self.functionParameters})(
   Description  ='{self.description}'
   Parameters   = {param}
   Interruptions= {self.interruptions}
   Returns      = {self.returns}
   Notes        = {self.notes}
        )"""
        