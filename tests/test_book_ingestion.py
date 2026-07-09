from app.ingestion.book_ingestion import BookIngestionEngine

def test_book_exists():
    engine = BookIngestionEngine("books/qawaed.pdf")
    info = engine.inspect()

    assert info["pages"] > 0
    assert info["contains_images"] is True