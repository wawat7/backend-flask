from queries import AbstractDatabase
import mysql.connector
from adapter.transform.book_transform import transform_book
from adapter.formatter.book_formatter import format_book
from schemas.book.create_book_schema import CreateBookSchema
from schemas.book.update_book_schema import UpdateBookSchema


class SqlDB(AbstractDatabase):
    __book_table__ = 'books_table'
    
    
    def __init__(self, host, port, database, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    def connect(self):
        db_config = {
            'host': self.host,
            'port': self.port,
            'user': self.username,
            'password': self.password,
            'database': self.database,
        }
        self.conn = mysql.connector.connect(**db_config)
        
    def normalize(self, book):
        return {
            "id": book[0],
            "name": book[1]
        }

    def find_books(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {self.__book_table__}")
        data = cursor.fetchall()
        cursor.close()
        return [format_book(self.normalize(book)) for book in data]
    
    def create_book(self, book: CreateBookSchema):
        cursor = self.conn.cursor()
        query = f"INSERT INTO {self.__book_table__} (name) VALUES (%s)"
        values = (book.name,)
        cursor.execute(query, values)
        self.conn.commit()
        book_id = cursor.lastrowid
        cursor.close()
        return book_id
    
    def find_by_id_book(self, id: str):
        cursor = self.conn.cursor()
        query = f"SELECT * FROM {self.__book_table__} WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)
        data = cursor.fetchone()
        cursor.close()
        if data:
            return format_book(self.normalize(data))
        else:
            return None
    
    def update_book_by_id(self, id: str, book: UpdateBookSchema):
        cursor = self.conn.cursor()
        query = f"UPDATE {self.__book_table__} SET name = %s WHERE id = %s"
        values = (book.name, id,)
        cursor.execute(query, values)
        self.conn.commit()
        
    def delete_book_by_id(self, id: str):
        cursor = self.conn.cursor()
        query = f"DELETE FROM {self.__book_table__} WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)
        self.conn.commit()
    
    