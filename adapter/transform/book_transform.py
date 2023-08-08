from models.book_model import Book


def transform_book(book: Book):
    return {
        "id": book.id,
        "name": book.name
    }
    

def transform_books(books: [Book]):
    return [transform_book(book) for book in books]