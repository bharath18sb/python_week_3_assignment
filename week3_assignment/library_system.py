class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"{self.book_id} | {self.title} by {self.author} [{status}]"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.book_id in self.books:
            raise ValueError("Book ID already exists.")
        self.books[book.book_id] = book

    def remove_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found.")
        del self.books[book_id]

    def issue_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found.")
        if self.books[book_id].is_issued:
            raise ValueError("Book is already issued.")
        self.books[book_id].is_issued = True

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found.")
        if not self.books[book_id].is_issued:
            raise ValueError("Book is already available.")
        self.books[book_id].is_issued = False

    def display_books(self):
        print("\n--- Library Books ---")
        for book in self.books.values():
            print(book)

if __name__ == "__main__":
    lib = Library()
    b1 = Book(101, "Python Basics", "John Doe")
    lib.add_book(b1)
    lib.display_books()
    lib.issue_book(101)
    lib.display_books()
    try:
        lib.issue_book(101)
    except ValueError as e:
        print(f"Error: {e}")
