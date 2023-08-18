from flask_restx import Api, fields

class RegisterModel:
    def swag(api: Api):
        return api.model('RegisterModel', {
            'name': fields.String(required=True, description='name of user'),
            'username': fields.String(required=True, description='username of user'),
            'password': fields.String(required=True, description='password of user'),
            'email': fields.String(required=True, description='email of user'),
    })