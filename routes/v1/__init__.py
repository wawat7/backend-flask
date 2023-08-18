from routes.v1.book_route import book_route
from routes.v1.authentication_route import authentication_route
from flask_restx import Api

def register_routes(api: Api, db):
    prefix = '/api/v1'

    book_route(api, db, prefix)
    authentication_route(api, db, prefix)
