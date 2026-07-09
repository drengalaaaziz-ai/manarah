from dataclasses import asdict

from app.analysis.document_analyzer import DocumentAnalyzer
from app.ingestion.book_ingestion import BookIngestionEngine
from app.page.page_extractor import PageExtractor
from app.services.image_preprocessor import ImagePreprocessor


class ManarahPipeline:

    def __init__(self, book_path: str):
        self.book_path = book_path

    def execute(self):

        print("=" * 60)
        print("MANARAH PIPELINE")
        print("=" * 60)

        # المرحلة الأولى: تحليل الكتاب
        ingestion = BookIngestionEngine(self.book_path)
        info = ingestion.inspect()

        analyzer = DocumentAnalyzer()
        info = analyzer.analyze(info)

        # المرحلة الثانية: استخراج الصفحة الأولى
        extractor = PageExtractor()

        image_path = extractor.extract_first_page(
            self.book_path
        )

        print("\nFirst page extracted successfully:")
        print(image_path)

        # المرحلة الثالثة: تحسين الصورة
        processor = ImagePreprocessor()

        cleaned_path = processor.process(
            image_path,
            "workspace/cleaned/page_001.png"
        )

        print("\nCleaned image created:")
        print(cleaned_path)

        # معلومات الكتاب
        print("\nBook Information\n")

        for key, value in asdict(info).items():
            print(f"{key:20}: {value}")

        print("\nPipeline Finished Successfully.")

        return info