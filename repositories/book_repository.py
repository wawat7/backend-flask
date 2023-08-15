from schemas.book.create_book_schema import CreateBookSchema
from schemas.book.update_book_schema import UpdateBookSchema
from datetime import datetime


class BookRepository:
    def __init__(self, database):
        self.database = database
        
        
    def get_all(self):
        return self.database.find_books()
    
    def create(self, book: CreateBookSchema):
        return self.database.create_book(book)
    
    def find_by_id(self, id: str):
        return self.database.find_by_id_book(id)
    
    def update_by_id(self, id: str, book: UpdateBookSchema):
        return self.database.update_book_by_id(id, book)
    
    def delete_by_id(self, id: str):
        return self.database.delete_book_by_id(id)