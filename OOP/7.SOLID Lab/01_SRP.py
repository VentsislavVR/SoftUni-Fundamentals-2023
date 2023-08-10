from typing import List, Union


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: [Book]):
        self.books.append(book)


    def find_book(self, title: str) -> Union[Book, str]:
        try:
            return [b for b in self.books if b.title == title][0]
        except IndexError:
            return "Book does not exist"


b1 = Book("Test1", "T1")
b2 = Book("Test2", "T2")
b3 = Book("Test3", "T3")

library = Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

print(library.find_book("Test1"))
