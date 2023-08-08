from queries import AbstractDatabase
from pymongo import MongoClient
from adapter.formatter.book_formatter import format_book
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

    def find_books(self):
        return [format_book(book) for book in self.client.books.find()]
    
