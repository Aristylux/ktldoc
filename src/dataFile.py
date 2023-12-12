from .function import Function

from enum import Enum

class FileType(Enum):
    UNKNOWN = 0
    CLASS = 1
    ENUM = 2
    FILE = 3

class DataFile:
    def __init__(self) -> None:
        self.fileName = ""
        self.extension = ""
        self.__type = FileType.UNKNOWN # class, file, class activity, enum, ...
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

    def setType(self, type: FileType):
        self.__type = type

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
    
    def getType(self) -> FileType:
        return self.__type

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