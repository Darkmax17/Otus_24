import csv
import json
import math


# Чтение книг из файла books.csv
def read_books(filename):
    books = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if all(key in row for key in ['Title', 'Author', 'Pages', 'Genre']):
                row['Pages'] = int(row['Pages'])
                books.append(row)
    print(f"Количество прочитанных книг: {len(books)}")  # Добавление логирования
    return books

def read_users(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        users = json.load(file)
    print(f"Количество прочитанных пользователей: {len(users)}")  # Добавление логирования
    return users



# Распределение книг между пользователями
def distribute_books(books, users):
    num_users = len(users)
    books_per_user = math.ceil(len(books) / num_users)

    result = []  # Новый список для хранения итоговых пользователей

    for i, user in enumerate(users):
        # Создание словаря для пользователя с необходимыми полями
        user_data = {
            "name": user['name'],
            "gender": user['gender'],
            "address": user['address'],
            "age": user['age'],
            "books": []
        }

        # Выбор книг для пользователя
        assigned_books = books[i * books_per_user:(i + 1) * books_per_user]

        # Форматирование книг в нужный вид
        user_data['books'] = [
            {
                "title": book['Title'],
                "author": book['Author'],
                "pages": book['Pages'],
                "genre": book['Genre']
            }
            for book in assigned_books
        ]

        result.append(user_data)  # Добавление пользователя в итоговый список

    return result


# Запись результата в result.json
def write_result(filename, data):
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# Основная функция
def main():
    books = read_books('books.csv')
    if not books:
        print("Нет книг для распределения.")  # Проверка на пустой список книг
        return

    users = read_users('users.json')
    if not users:
        print("Нет пользователей для распределения книг.")  # Проверка на пустой список пользователей
        return

    result = distribute_books(books, users)
    if not result:
        print("Не удалось распределить книги между пользователями.")  # Проверка на пустой результат распределения

    write_result('result.json', result)
    print("Результат успешно записан в result.json.")


if __name__ == "__main__":
    main()