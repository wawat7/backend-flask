from queries.mongo import MongoDB
from queries.sql import SqlDB
from repositories.book_repository import BookRepository
from flask import Flask
from routes.v1 import register_routes
from flask_restx import Api


def create_app():

    # database = MongoDB(**{
    #     "host": "localhost",
    #     "port": 27018,
    #     "database": "bookstore",
    #     "username": "mongo",
    #     "password": "mongo"
    # })
    
    database = SqlDB(**{
        "host": "localhost",
        "port": 3306,
        "database": "bookstore",
        "username": "root",
        "password": "root"
    })
    
    database.connect()
    
    
    # bookRepository = BookRepository(database)
    
    app = Flask(__name__)
    api = Api(app)

    register_routes(api, database)

    @app.get("/")
    def main():
        return {"message": "app running well..."}

    return app