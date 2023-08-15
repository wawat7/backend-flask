from flask import Flask, request, Blueprint
from controllers.book_controller import BookController
from flask_restx import Api, Resource, Namespace, fields
from adapter.swagger.models.book.create_book_model import CreateBookModel
from adapter.swagger.models.book.update_book_model import UpdateBookModel


def book_route(api: Api, db, prefix):
    controller = BookController(db)
    
    book_namespace = Namespace('Book', path=f'{prefix}/books', description="List endpoint books")
    
    @book_namespace.route('/')
    class BookList(Resource):
        @book_namespace.doc(description="Get all books")
        def get(self):
            return controller.get_all_books()

        @book_namespace.doc(description="Create a new book")
        @book_namespace.expect(CreateBookModel.swag(api))
        def post(self):
            return controller.create_book(request)
        
        
    @book_namespace.route('/<id>')
    class BookDetail(Resource):
        @book_namespace.doc(description="get book by id")
        def get(self, id: str):
            return controller.find_by_id(id)
            
        @book_namespace.doc(description="update book by id")
        @book_namespace.expect(UpdateBookModel.swag(api))
        def put(self, id: str):
            return controller.update_book_by_id(id, request)

        @book_namespace.doc(description="delete book by id")
        def delete(self, id: str):
            return controller.delete_book_by_id(id)  
        
    api.add_namespace(book_namespace)
    