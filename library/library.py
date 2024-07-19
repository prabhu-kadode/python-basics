class Library:
    def __init__(self):
        self.list_Of_books = []
    def add_book(self,book):
        self.list_Of_books.append(book)
    def show_all_books(self):
        print(self.list_Of_books)

library = Library()

books  = [
    {
        "name":"A",
        "author":"pra",
        "totalPages":200,
    },
    {
        "name":"B",
        "author":"pra",
        "totalPages":200,
    }
]
BOOK_ID_START_POINT = 100
for index,book in enumerate(books):
    book.update({"id":BOOK_ID_START_POINT+index})
    library.add_book(book)
library.show_all_books()
