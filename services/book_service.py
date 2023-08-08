from repositories.book_repository import BookRepository


class BookService:
    
    def __init__(self, book_repo: BookRepository):
        self.repo = book_repo
    
    
    def get_all(self):
        return self.repo.get_all()