from app.ingestion.book_ingestion import BookIngestionEngine

book = BookIngestionEngine("books/qawaed.pdf")

print(book.inspect())