from flask import Flask, request, Blueprint
from controllers.user_controller import UserController
from flask_restx import Api, Resource, Namespace, fields
from adapter.swagger.models.authentication.login_model import LoginModel
from adapter.swagger.models.authentication.register_model import RegisterModel


def authentication_route(api: Api, db, prefix):
    controller = UserController(db)
    
    user_namespace = Namespace('Authentication', path=f'{prefix}/auth', description="List endpoint authentication")
    
    @user_namespace.route('/login')
    class UserLogin(Resource):
        @user_namespace.doc(description="Login user")
        @user_namespace.expect(LoginModel.swag(api))
        def post(self):
            return controller.login(request)
        
        
    @user_namespace.route('/register')
    class UserRegistration(Resource):
        @user_namespace.doc(description="Register User")
        @user_namespace.expect(RegisterModel.swag(api))
        def post(self):
            return controller.register(request)

        
    api.add_namespace(user_namespace)
    