from models.book_model import Book


def format_book(book):
    return Book(**{
        "id": book['id'],
        "name": book['name']
    })
    
def format_books(books):
    formats = []
    for book in books:
        formats.append(book)
        
    return formats