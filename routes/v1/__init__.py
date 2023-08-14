from routes.v1.book_route import book_route
from flask_restx import Api

def register_routes(api: Api, db):
    prefix = '/api/v1'

    book_route(api, db, prefix)
