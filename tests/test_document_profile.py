from pathlib import Path

from app.models.document_profile import DocumentProfile


def test_document_profile():

    profile = DocumentProfile(
        name="book.pdf",
        path=Path("book.pdf"),
        extension=".pdf",
        size_mb=12.5,
        pages=100,
        encrypted=False,
        contains_text=False,
        contains_images=True,
        page_width=612,
        page_height=792,
        needs_ocr=True
    )

    assert profile.pages == 100
    assert profile.needs_ocr