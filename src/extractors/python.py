from src.extractors.extractorInterface import ExtractorInterface


class PythonExtractor(ExtractorInterface):

    def extract(self, str):
        print("Extract Python")