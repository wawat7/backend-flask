from queries import AbstractDatabase
from pymongo import MongoClient
from adapter.formatter.book_formatter import format_book
from schemas.book.create_book_schema import CreateBookSchema
from schemas.book.update_book_schema import UpdateBookSchema
from bson.objectid import ObjectId
from schemas.user.create_user_schema import CreateUserSchema

class MongoDB(AbstractDatabase):
    def __init__(self, host, port, database, username, password):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.client = None
        self.collection = None

    def connect(self):
        self.client = MongoClient(**{
            "host": self.host,
            "port":  self.port,
            "username": self.username,
            "password": self.password
        })
        self.client = self.client[self.database]
        
    def normalize(self, book):
        return {
            "id": str(book['_id']),
            "name": book['name'],
            "created_at": book['created_at'] if 'created_at' in book else None,
            "updated_at": book['updated_at'] if 'updated_at' in book else None,
        }

    def find_books(self):
        return [format_book(self.normalize(book)) for book in self.client.books.find()]
    
    def create_book(self, book: CreateBookSchema):
        return self.client.books.insert_one({
            "name": book.name,
            "created_at": book.created_at,
            "updated_at": book.updated_at
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
                "name": book.name,
                "updated_at": book.updated_at
            }
        })
        
    def delete_book_by_id(self, id: str):
        return self.client.books.delete_one({
            "_id": ObjectId(id)
        })
        
    def create_user(self, user: CreateUserSchema):
        return self.client.users.insert_one({
            "name": user.name,
            "username": user.username,
            "password": user.password,
            "email": user.email,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        }).inserted_id
        
    def find_by_id_user(self, id: str):
        return self.client.users.find_one({
            "_id": ObjectId(id)
        })
        
    def find_by_username_user(self, username: str):
        return self.client.users.find_one({
            "username": username
        })
    
    
        
    
