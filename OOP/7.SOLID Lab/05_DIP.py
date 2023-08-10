from abc import ABC, abstractmethod


class Book:
    def __init__(self, tittle, author, content: str):
        self.content = content
        self.title = tittle
        self.author = author


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class PaperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.title}\n{book.author}\n{book.content[:4]}"


class WebFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.title}\n{book.author}\n{book.content}"


class Printer:
    def __init__(self, formatter: BaseFormatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)

book = Book("FIRST","HIM","CONTEND")
pa = Printer(PaperFormatter())
pb = Printer(WebFormatter())
print(pa.get_book(book))
