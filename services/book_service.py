from repositories.book_repository import BookRepository
from schemas.book.create_book_schema import CreateBookSchema
from schemas.book.update_book_schema import UpdateBookSchema
from datetime import datetime

class BookService:
    
    def __init__(self, book_repo: BookRepository):
        self.repo = book_repo
    
    
    def get_all(self):
        return self.repo.get_all()
    
    def create(self, book: CreateBookSchema):
        book.created_at = datetime.now()
        book.updated_at = datetime.now()
        return self.repo.create(book)
    
    def find_by_id(self, id: str):
        return self.repo.find_by_id(id)
    
    def update_by_id(self, id: str, book: UpdateBookSchema):
        book.updated_at = datetime.now()
        return self.repo.update_by_id(id, book)
    
    def delete_by_id(self, id: str):
        return self.repo.delete_by_id(id)