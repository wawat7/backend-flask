from flask_restx import Api, fields

class CreateBookModel:
    def swag(api: Api):
        return api.model('CreateBookModel', {
            'name': fields.String(required=True, description='Name of the book'),
    })