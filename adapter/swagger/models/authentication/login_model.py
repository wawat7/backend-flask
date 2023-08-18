from flask_restx import Api, fields

class LoginModel:
    def swag(api: Api):
        return api.model('LoginModel', {
            'username': fields.String(required=True, description='username of user'),
            'password': fields.String(required=True, description='password of user'),
    })