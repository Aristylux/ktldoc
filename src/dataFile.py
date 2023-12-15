from .function import Function

from enum import Enum

class FileType(Enum):
    UNKNOWN = 0
    CLASS = 1
    ENUM = 2
    FILE = 3

class RawData:
    def __init__(self) -> None:
        self.comment = ""
        self.function = ""
        pass

class DataFile:
    def __init__(self) -> None:
        self.fileName = ""
        self.__extension = ""
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
        self.__extension = extension

    def setType(self, type: FileType):
        self.__type = type

    def setDescription(self, description: str):
        self.__description = description
        self.__hasDescription = True

    def addRawData(self, comment: str, function: str):
        raw = RawData()
        raw.comment = comment
        raw.function = function
        self.__rawData.append(raw)

    def addFunction(self, function: Function):
        self.functions.append(function)

    # -- Getters --

    def getFileName(self) -> str:
        return self.fileName
    
    def getExtension(self) -> str:
        return self.__extension
    
    def getType(self) -> FileType:
        return self.__type

    def getDescription(self) -> str:
        return self.__description

    def hasDescription(self) -> bool:
        return self.__hasDescription

    def getRawData(self) -> list[RawData]:
        return self.__rawData
    
    def getFunctions(self) -> list[Function]:
        return self.functions
    

    def __str__(self) -> str:
        return f"{self.fileName}{self.extension} - {self.functions}"