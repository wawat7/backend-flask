from queries import AbstractDatabase
import mysql.connector
from adapter.transform.book_transform import transform_book
from utils.formatter.book_formatter import format_book

class SqlDB(AbstractDatabase):
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database

    def connect(self):
        db_config = {
            'host': self.host,
            'port': self.port,
            'user': 'root',
            'password': 'root',
            'database': self.database,
        }
        self.conn = mysql.connector.connect(**db_config)

    def find_books(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM books_table")
        data = cursor.fetchall()
        cursor.close()
        return [format_book(self.normalize(book)) for book in data]
    
    def normalize(self, book):
        return {
            "id": book[0],
            "name": book[1]
        }