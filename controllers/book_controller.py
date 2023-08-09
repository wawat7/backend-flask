from repositories.book_repository import BookRepository
from services.book_service import BookService
from adapter.transform.book_transform import transform_book, transform_books
from schemas.book.create_book_schema import CreateBookSchema
from schemas.book.update_book_schema import UpdateBookSchema
from flask import request

class BookController:
    book_repo: BookRepository
    book_service: BookService
    
    def __init__(self, db):
        self.book_repo = BookRepository(db)
        self.book_service = BookService(self.book_repo)
        
    
    def get_all_books(self):
        return transform_books(self.book_service.get_all())
    
    def find_by_id(self, id: str):
        return transform_book(self.book_service.find_by_id(id))
    
    def create_book(self, request: request):
        payload = request.get_json()
        inserted_id = self.book_service.create(CreateBookSchema(**{
            "name": payload['name']
        }))
        return transform_book(self.book_service.find_by_id(inserted_id))
    
    def update_book_by_id(self, id: str, request: request):
        payload = request.get_json()
        self.book_service.update_by_id(id, UpdateBookSchema(**{
            "name": payload['name']
        }))
        return transform_book(self.book_service.find_by_id(id))
    
    def delete_book_by_id(self, id: str):
        self.book_service.delete_by_id(id)
        