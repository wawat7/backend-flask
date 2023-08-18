from repositories.user_repository import UserRepository
from schemas.user.create_user_schema import CreateUserSchema
from datetime import datetime, timedelta
from utils.hash_utils import hash_string, check_hash_string
from schemas.user.login_schema import LoginSchema
from configs.environment_config import get_environment_variables
import jwt

class UserService:
    repo: UserRepository
    env: dict
    
    def __init__(self, repo: UserRepository):
        self.repo = repo
        self.env = get_environment_variables()
        
        
    def register(self, user: CreateUserSchema):
        user.created_at = datetime.now()
        user.updated_at = datetime.now()
        user.password = hash_string(user.password)
        return self.repo.create(user)
    
    def login(self, login: LoginSchema):
        user = self.repo.find_by_username(**{
            "username": login.username
        })
        
        checkPassword = check_hash_string(login.password, user['password'])
        if not checkPassword:
            raise Exception('password is wrong !')
        
        expired_time = datetime.utcnow() + timedelta(hours=1)
        payload = {
            'username': login.username,
            'exp': expired_time
        }
        token = jwt.encode(payload, self.env['JWT_SECRET_KEY'], algorithm='HS256')
        return {
            "token": token,
        }
        
        
        ##VERIFY TOKEN
        # decoded_payload = jwt.decode(token, self.env['JWT_SECRET_KEY'], algorithms=['HS256'])
        
    
        
        