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

def remove_book():
    name_of_book = input("Введите название книги для удаления: ")

    file = open("catalog.txt", "r", encoding="utf-8")
    books = file.readlines()
    file.close()

    updated_books = []
    book_found = False

    for book in books:
        current_name_of_book = book.split(';')[0]
        if current_name_of_book != name_of_book:
            updated_books.append(book)
        else:
            book_found = True

    file = open("catalog.txt", "w", encoding="utf-8")
    file.writelines(updated_books)
    file.close()

    if book_found:
        print("Книга удалена из каталога")
    else:
        print("Книга не найдена в каталоге")

def edit_book():
    name_of_book = input("Введите название книги для редактирования: ")

    file = open("catalog.txt", "r", encoding="utf-8")
    books = file.readlines()
    file.close()

    updated_books = []
    book_found = False

    for book in books:
        current_name_of_book = book.split(';')[0]
        if current_name_of_book == name_of_book:
            book_found = True
            print("Текущая информация о книге:")
            print(book.strip())

            new_name = input("Введите новое название книги (оставьте пустым, если изменения не нужны)")
            new_author = input("Введите нового автора (оставьте пустым, если изменения не нужны): ")
            new_year = input("Введите новый год издания (оставьте пустым, если изменения не нужны): ")
            new_genre = input("Введите новый жанр (оставьте пустым, если изменения не нужны): ")
            new_count = input("Введите новое количество книг (оставьте пустым, если изменения не нужны): ")

            if new_name:
                current_name_of_book = new_name

            if new_author:
                author = new_author
            else:
                author = book.split(';')[1]

            if new_year:
                year_of_publication = new_year
            else:
                year_of_publication = book.split(';')[2]

            if new_genre:
                genre = new_genre
            else:
                genre = book.split(';')[3]

            if new_count:
                count_books = new_count
            else:
                count_books = book.split(';')[4].strip()

            updated_book = f"{current_name_of_book};{author};{year_of_publication};{genre};{count_books}\n"
            updated_books.append(updated_book)
        else:
            updated_books.append(book)

    file = open("catalog.txt", "w", encoding="utf-8")
    file.writelines(updated_books)
    file.close()

    if book_found:
        print("Информация о книге обновлена")
    else:
        print("Книга не найдена в каталоге")