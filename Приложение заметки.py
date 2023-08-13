# Импортируем модуль для работы с файлами
import os

# Определяем функцию для создания новой заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")

    # Создаем новый файл для заметки
    with open(f"{title}.txt", "w") as file:
        file.write(content)
    print("Заметка успешно создана!")

# Определяем функцию для просмотра всех заметок
def view_notes():
    files = os.listdir()  # Получаем список всех файлов в текущей директории

    # Отображаем все файлы, которые являются заметками
    for file in files:
        if file.endswith(".txt"):
            with open(file, "r") as note:
                print(f"--- Заметка: {file} ---")
                print(note.read())
                print("--------------------")

# Определяем функцию для удаления заметки
def delete_note():
    title = input("Введите заголовок заметки, которую хотите удалить: ")

    # Проверяем, существует ли файл с таким заголовком и удаляем его, если да
    if os.path.isfile(f"{title}.txt"):
        os.remove(f"{title}.txt")
        print("Заметка успешно удалена!")
    else:
        print("Заметка с таким заголовком не найдена.")

# Основной код
while True:
    print("1. Создать новую заметку")
    print("2. Просмотреть все заметки")
    print("3. Удалить заметку")
    print("4. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        break  # Выходим из цикла и завершаем программу
    else:
        print("Неверный выбор. Попробуйте еще раз.")