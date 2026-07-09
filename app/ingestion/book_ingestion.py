from pathlib import Path

import fitz  # PyMuPDF

from app.models.document_profile import DocumentProfile


class BookIngestionEngine:
    """
    MANARAH - Book Ingestion Engine
    مسؤوليته:
    - فتح الكتاب
    - فحصه
    - إنشاء DocumentProfile
    """

    def __init__(self, book_path: str):
        self.book_path = Path(book_path)

    def inspect(self) -> DocumentProfile:

        if not self.book_path.exists():
            raise FileNotFoundError(f"Book not found: {self.book_path}")

        doc = fitz.open(self.book_path)

        pages = len(doc)

        contains_text = False
        contains_images = False

        for page in doc:

            if page.get_text().strip():
                contains_text = True

            if page.get_images():
                contains_images = True

            if contains_text and contains_images:
                break

        first_page = doc[0]

        profile = DocumentProfile(

            name=self.book_path.name,

            path=self.book_path,

            extension=self.book_path.suffix,

            size_mb=round(
                self.book_path.stat().st_size / (1024 * 1024),
                2
            ),

            pages=pages,

            encrypted=doc.is_encrypted,

            contains_text=contains_text,

            contains_images=contains_images,

            page_width=round(first_page.rect.width, 2),

            page_height=round(first_page.rect.height, 2),

            needs_ocr=not contains_text,

            document_type="PDF"
        )

        doc.close()

        return profile