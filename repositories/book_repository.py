class BookRepository:
    def __init__(self, database):
        self.database = database
        
        
    def get_all(self):
        return self.database.find_books()