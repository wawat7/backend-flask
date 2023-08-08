from routes.v1.book_route import book_route
from flask import Flask

def register_routes(app: Flask, db):
    prefix = '/api/v1'

    book_route(app, db, prefix)



