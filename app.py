from queries.mongo import MongoDB
from queries.sql import SqlDB
from repositories.book_repository import BookRepository


def create_app():

    database = MongoDB(**{
        "host": "localhost",
        "port": 27018,
        "database": "bookstore",
    })
    
    # database = SqlDB(**{
    #     "host": "localhost",
    #     "port": 3306,
    #     "database": "bookstore"
    # })
    
    database.connect()
    
    bookRepository = BookRepository(database)
    
    for book in bookRepository.get_all():
        print(book.id)
    
    
    
create_app()