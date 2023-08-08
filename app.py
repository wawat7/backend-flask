from queries.mongo import MongoDB
from queries.sql import SqlDB
from repositories.book_repository import BookRepository
from flask import Flask
from routes.v1 import register_routes

def create_app():

    # database = MongoDB(**{
    #     "host": "localhost",
    #     "port": 27018,
    #     "database": "bookstore",
    # })
    
    # database = SqlDB(**{
    #     "host": "localhost",
    #     "port": 3306,
    #     "database": "bookstore"
    # })
    
    database.connect()
    
    
    # bookRepository = BookRepository(database)
    
    app = Flask(__name__)

    register_routes(app, database)

    @app.get("/")
    def main():
        return {"message": "app running well..."}

    return app
    
    
    
    
    
create_app()