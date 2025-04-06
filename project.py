def add_book():
    name_of_book = input("Введите название книги: ")
    author = input("Ввеите автора книги: ")
    year_of_publication = int(input("Введите год издания книги: "))
    genre = input("Введите жанр книги: ")
    count_books = int(input("Введите количество кинг в наличии: "))

    book = f"{name_of_book}; {author}; {year_of_publication}; {genre}; {count_books}"

    file = open("catalog.txt", "a", encoding="utf-8")
    file.write(book)
    file.close()

    print("Книга добавлена в каталог")

