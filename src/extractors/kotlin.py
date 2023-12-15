from src.extractors.extractorInterface import ExtractorInterface


class KotlinExtractor(ExtractorInterface):

    def extract(self, str):
        print("Extract Kotlin")