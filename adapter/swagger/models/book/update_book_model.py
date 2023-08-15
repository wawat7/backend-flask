from flask_restx import Api, fields

class UpdateBookModel:
    def swag(api: Api):
        return api.model('UpdateBookModel', {
            'name': fields.String(required=True, description='Name of the book'),
    })