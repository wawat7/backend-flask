from repositories.book_repository import BookRepository
from services.book_service import BookService
from adapter.transform.book_transform import transform_book, transform_books
from schemas.book.create_book_schema import CreateBookSchema
from schemas.book.update_book_schema import UpdateBookSchema
from flask import request
from adapter.response.success_response import success_response
from adapter.requests.book.create_book_request import CreateBookValidator
from adapter.response.bad_request import bad_request_response
from queries.mongo import MongoDB
from utils.object_id_utils import is_valid_objectid

class BookController:
    book_repo: BookRepository
    book_service: BookService
    database: any
    
    def __init__(self, db):
        self.book_repo = BookRepository(db)
        self.book_service = BookService(self.book_repo)
        self.database = db
        
    
    def get_all_books(self):
        return success_response(transform_books(self.book_service.get_all()), 'list books')
    
    def find_by_id(self, id: str):
        if isinstance(self.database, MongoDB) and not is_valid_objectid(id):
            return bad_request_response('id not valid', {})
            
        return success_response(transform_book(self.book_service.find_by_id(id)), 'detail book')
    
    def create_book(self, request: request):
        validator = CreateBookValidator(request)
        
        if not validator.validate():
            return bad_request_response('BAD REQUEST', validator.errors)
        
        payload = request.get_json()
        inserted_id = self.book_service.create(CreateBookSchema(**{
            "name": payload['name']
        }))
        return success_response(transform_book(self.book_service.find_by_id(inserted_id)), 'create book successfully')
    
    def update_book_by_id(self, id: str, request: request):
        if isinstance(self.database, MongoDB) and not is_valid_objectid(id):
            return bad_request_response('id not valid', {})
        
        validator = CreateBookValidator(request)
        
        if not validator.validate():
            return bad_request_response('BAD REQUEST', validator.errors)
        
        payload = request.get_json()
        self.book_service.update_by_id(id, UpdateBookSchema(**{
            "name": payload['name']
        }))
        return success_response(transform_book(self.book_service.find_by_id(id)), 'update book successfully')
    
    def delete_book_by_id(self, id: str):
        self.book_service.delete_by_id(id)
        return success_response({}, 'delete book successfully')
        