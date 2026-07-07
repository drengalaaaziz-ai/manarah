from pathlib import Path
import fitz  # PyMuPDF


class BookIngestionEngine:
    """
    MANARAH - Book Ingestion Engine v0.0.2
    """

    def __init__(self, book_path):
        self.book_path = Path(book_path)

    def inspect(self):

        if not self.book_path.exists():
            raise FileNotFoundError(f"Book not found: {self.book_path}")

        doc = fitz.open(self.book_path)

        page_count = len(doc)

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

        width = round(first_page.rect.width, 2)
        height = round(first_page.rect.height, 2)

        info = {

            "name": self.book_path.name,

            "extension": self.book_path.suffix,

            "size_mb": round(
                self.book_path.stat().st_size / (1024 * 1024), 2
            ),

            "pages": page_count,

            "encrypted": doc.is_encrypted,

            "contains_text": contains_text,

            "contains_images": contains_images,

            "page_size_points": f"{width} × {height}"

        }

        doc.close()

        return info