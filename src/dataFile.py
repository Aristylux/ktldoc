from .function import Function

class DataFile:
    def __init__(self) -> None:
        self.fileName = ""
        self.extension = ""
        self.description = ""
        self.functions = [Function]

        self.__rawData = []
        pass

    def setFilename(self, fileName: str):
        self.fileName = fileName

    def setExtension(self, extension: str):
        self.extension = extension

    def addRawData(self, comment: str, function: str):
        self.__rawData.append([comment, function])

    def getRawData(self):
        return self.__rawData