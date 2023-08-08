from repositories.book_repository import BookRepository
from services.book_service import BookService
from adapter.transform.book_transform import transform_book, transform_books



class BookController:
    book_repo: BookRepository
    book_service: BookService
    
    def __init__(self, db):
        self.book_repo = BookRepository(db)
        self.book_service = BookService(self.book_repo)
        
    
    def get_all_books(self):
        return transform_books(self.book_service.get_all())