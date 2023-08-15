from datetime import datetime

class Book:
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    
    def __init__(self, id, name, created_at = None, updated_at = None):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        