from src.dataFile import DataFile

class ExtractorInterface:
    def extract(self, filePath: str, datafile: DataFile):
        raise NotImplementedError("Subclasses must implement the format method")
