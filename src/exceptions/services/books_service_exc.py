

class BookNotFoundServiceException(Exception):
    def __init__(self, book_uuid: str):
        self.book_uuid = book_uuid
