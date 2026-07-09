from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class DocumentProfile:
    """
    يمثل أي وثيقة تدخل إلى MANARAH.
    """

    name: str
    path: Path
    extension: str

    size_mb: float

    pages: int

    encrypted: bool

    contains_text: bool

    contains_images: bool

    page_width: float

    page_height: float

    language: str = "Unknown"

    needs_ocr: bool = False

    document_type: str = "Unknown"

    def summary(self):
        return (
            f"{self.name} | "
            f"{self.pages} pages | "
            f"OCR={self.needs_ocr}"
        )