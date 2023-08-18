from datetime import datetime


class CreateUserSchema:
    name: str
    username: str
    password: str
    email: str
    created_at: datetime
    updated_at: datetime
    
    def __init__(self, name: str, username: str, password: str, email: str, created_at: datetime = None, updated_at: datetime = None):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at