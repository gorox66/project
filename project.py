class Book:
    def __init__(self, title, author, year, genre, quantity):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.quantity = quantity

    def __str__(self):
        return f"{self.title};{self.author};{self.year};{self.genre};{self.quantity}"

def add_book(book):
    file = open('catalog.txt', 'a', encoding='utf-8')
    file.write(str(book) + '\n')
    file.close()