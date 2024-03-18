from src.dataFile import DataFile, RawData

class ExtractorInterface:
    def extract(self, filePath: str, datafile: DataFile):
        raise NotImplementedError("Subclasses must implement the format method")
    
    def extractFunction(self, rawData: RawData, data: DataFile):
        raise NotImplementedError("Subclasses must implement the format method")
