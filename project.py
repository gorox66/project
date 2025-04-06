def add_book():
    name_of_book = input("Введите название книги: ")
    author = input("Ввеите автора книги: ")
    year_of_publication = int(input("Введите год издания книги: "))
    genre = input("Введите жанр книги: ")
    count_books = int(input("Введите количество кинг в наличии: "))

    book = f"{name_of_book};{author};{year_of_publication};{genre};{count_books}\n"

    file = open("catalog.txt", "a", encoding="utf-8")
    file.write(book)
    file.close()

    print("Книга добавлена в каталог")

def show_books():
    file = open("catalog.txt", "r", encoding="utf-8")
    books = file.readlines()
    file.close()

    if books:
        print("Список книг:")
        for book in books:
            name_of_book, author, year_of_publication, genre, count_books = book.strip().split(';')
            print(f"Название книги: {name_of_book}, автор: {author}, год издания: {year_of_publication}, жанр: {genre}, количество книг в наличии: {count_books}")
    else:
        print("В каталоге нет книг")
