class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f'"{self.title}" by {self.author}'


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.checked_out_books = []

    def checkout_book(self, book):
        self.checked_out_books.append(book)

    def return_book(self, book):
        if book in self.checked_out_books:
            self.checked_out_books.remove(book)


class Library:
    def __init__(self):
        self.books = []  # Available books
        self.members = []
        self.checked_out = {}  # book -> member

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def is_book_available(self, book):
        return book in self.books

    def checkout_book(self, book, member):
        if book in self.books:
            self.books.remove(book)
            self.checked_out[book] = member
            member.checkout_book(book)
        else:
            print(f"Book {book} is not available.")

    def return_book(self, book, member):
        if self.checked_out.get(book) == member:
            self.books.append(book)
            del self.checked_out[book]
            member.return_book(book)
        else:
            print(f"Book {book} was not checked out by {member.name}.")

library = Library()
book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Structures", "Jane Doe")

library.add_book(book1)
library.add_book(book2)

member = Member("Alice", "M001")
library.register_member(member)

library.checkout_book(book1, member)
print(library.is_book_available(book1))  # Should return False
print(library.is_book_available(book2))  # Should return True

library.return_book(book1, member)
print(library.is_book_available(book1))  # Should return True