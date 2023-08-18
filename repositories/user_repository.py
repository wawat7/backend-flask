from schemas.user.create_user_schema import CreateUserSchema


class UserRepository:
    def __init__(self, database):
        self.database = database
        
        
    def create(self, user: CreateUserSchema):
        return self.database.create_user(user)
    
    def find_by_username(self, username: str):
        return self.database.find_by_username_user(username)
        
        
        