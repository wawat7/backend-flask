from repositories.user_repository import UserRepository
from services.user_service import UserService
from flask import request
from adapter.response.success_response import success_response
from adapter.transform.register_transform import transform_register
from adapter.transform.login_transform import transform_login
from schemas.user.create_user_schema import CreateUserSchema
from schemas.user.login_schema import LoginSchema

class UserController:
    book_repo: UserRepository
    book_service: UserService
    database: any
    
    def __init__(self, db):
        self.database = db
        self.book_repo = UserRepository(db)
        self.book_service = UserService(self.book_repo)
        
        
    def register(self, req: request):
        payload = req.get_json()
        self.book_service.register(CreateUserSchema(**{
            "name": payload['name'],
            "username": payload['username'],
            "password": payload['password'],
            "email": payload['email']
        }))
        return success_response(transform_register(), 'register user successfully')
    
    
    def login(self, req: request):
        payload = req.get_json()
        token = self.book_service.login(LoginSchema(**{
            "username": payload['username'],
            "password": payload['password']
        }))
        return transform_login(token['token'])