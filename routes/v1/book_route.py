from flask import Flask, request, Blueprint
from controllers.book_controller import BookController
from schemas.book.create_book_schema import CreateBookSchema


def book_route(app: Flask, db, prefix):
    controller = BookController(db)
    book_blueprint = Blueprint('books', __name__)

    @book_blueprint.route('/', methods=['GET'])
    def get_all_books():
        return controller.get_all_books()

    @book_blueprint.route('/<id>', methods=['GET'])
    def get_book_by_id(id: str):
        return controller.find_by_id(id)

    @book_blueprint.route('/', methods=['POST'])
    def create_book():
        return controller.create_book(request)

    @book_blueprint.route('/<id>', methods=['PUT'])
    def update_book(id: str):
        return controller.update_book_by_id(id, request)

    @book_blueprint.route('/<id>', methods=['DELETE'])
    def delete_book(id: str):
        controller.delete_book_by_id(id)
        return {}

    app.register_blueprint(book_blueprint, url_prefix=f"{prefix}/books")
