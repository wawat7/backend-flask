from datetime import datetime


class CreateBookSchema:
    name: str
    created_at: datetime
    updated_at: datetime
    
    def __init__(self, name: str, created_at: datetime = None, updated_at: datetime = None):
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at