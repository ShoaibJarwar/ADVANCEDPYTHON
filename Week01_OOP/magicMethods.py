class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title}, {self.pages} pages"

    def __len__(self):
        return self.pages

book = Book("Python 101", 350)
print(book)       # Python 101, 350 pages
print(len(book))  # 350

book2 = Book("Python Pandas", 1256)
print(book2)
print(len(book2))