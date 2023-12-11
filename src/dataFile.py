from .function import Function

class DataFile:
    def __init__(self) -> None:
        self.fileName = ""
        self.extension = ""
        #self.type = "" # class, file, class activity, enum, ...
        self.__description = ""
        self.__hasDescription = False
        self.functions = []

        self.__rawData = []
        pass

    # -- Setters --

    def setFilename(self, fileName: str):
        self.fileName = fileName

    def setExtension(self, extension: str):
        self.extension = extension

    def setDescription(self, description: str):
        self.__description = description
        self.__hasDescription = True

    def addRawData(self, comment: str, function: str):
        self.__rawData.append([comment, function])

    def addFunction(self, function: Function):
        self.functions.append(function)

    # -- Getters --

    def getFileName(self) -> str:
        return self.fileName
    
    def getDescription(self) -> str:
        return self.__description

    def hasDescription(self) -> bool:
        return self.__hasDescription

    def getRawData(self):
        return self.__rawData
    
    def getFunctions(self) -> list[Function]:
        return self.functions
    

    def __str__(self) -> str:
        return f"{self.fileName}{self.extension} - {self.functions}"