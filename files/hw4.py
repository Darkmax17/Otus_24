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

    filtered_users = []  # Новый список для хранения отфильтрованных пользователей
    for user in users:
        if all(key in user for key in ['name', 'gender', 'address', 'age']):
            filtered_user = {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age']
            }
            filtered_users.append(filtered_user)

    print(f"Количество прочитанных пользователей: {len(filtered_users)}")  # Добавление логирования
    return filtered_users


# Распределение книг между пользователями
def distribute_books(books, users):
    num_users = len(users)
    total_books = len(books)

    # Определяем, сколько книг каждый пользователь должен получить
    base_books_per_user = total_books // num_users
    extra_books_count = total_books % num_users  # Дополнительные книги, которые нужно распределить

    result = [dict(user) for user in users]  # Копируем данные о пользователях

    # Обнуляем список книг у каждого пользователя
    for user in result:
        user['books'] = []

    # Индекс для текущей книги
    book_index = 0

    for i in range(num_users):
        # Определяем количество книг для текущего пользователя
        books_for_user = base_books_per_user + (1 if i < extra_books_count else 0)

        for _ in range(books_for_user):
            if book_index < total_books:
                result[i]['books'].append({
                    "title": books[book_index]['Title'],
                    "author": books[book_index]['Author'],
                    "pages": books[book_index]['Pages'],
                    "genre": books[book_index]['Genre']
                })
                book_index += 1

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
