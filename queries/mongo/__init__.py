from queries import AbstractDatabase
from pymongo import MongoClient
from utils.formatter.book_formatter import format_book
from schemas.book.create_book_schema import CreateBookSchema
from schemas.book.update_book_schema import UpdateBookSchema
from bson.objectid import ObjectId
class MongoDB(AbstractDatabase):
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        self.client = None
        self.collection = None

    def connect(self):
        self.client = MongoClient(**{
            "host": self.host,
            "port":  self.port,
            "username": "mongo",
            "password": "mongo"
        })
        self.client = self.client[self.database]
        
    def normalize(self, book):
        return {
            "id": str(book['_id']),
            "name": book['name']
        }

    def find_books(self):
        return [format_book(self.normalize(book)) for book in self.client.books.find()]
    
    def create_book(self, book: CreateBookSchema):
        return self.client.books.insert_one({
            "name": book.name
        }).inserted_id
    
    def find_by_id_book(self, id: str):
        book = self.client.books.find_one({
            "_id": ObjectId(id)
        })
        return format_book(self.normalize(book))
    
    def update_book_by_id(self, id: str, book: UpdateBookSchema):
        return self.client.books.update_one({
            "_id": ObjectId(id),
        }, {
            "$set": {
                "name": book.name
            }
        })
        
    def delete_book_by_id(self, id: str):
        return self.client.books.delete_one({
            "_id": ObjectId(id)
        })
    
    
        
    
