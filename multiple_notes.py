from pprint import pprint
import datetime
print("Добро пожаловать в `Менеджер заметок`! Вы можете добавить новую заметку")
notes = []  # создаем пустой список для заметок
while True:
    username = input("Имя пользователя ")
    title = input("Заголовок заметки ")
    content = input("Описание заметки ")
    initial_status = input("Статус заметки ")
    print({"Текущий статус заметки ": initial_status})
    while True:
        status = input("Выберите новый статус заметки  1:новая, 2:в процессе, 3:выполнено ")
        if status in ["1", "новая"]:
            status = "Новая"
            print("Текущий статус заметки: Новая")
            break
        elif status in ["2", "в процессе"]:
            status = "В процессе"
            print("Текущий статус заметки: В процессе")
            break
        elif status in ["3", "выполнено"]:
            status = "Выполнено"
            print("Текущий статус заметки: Выполнено")
            break
        else:
            print("Некорректно введен статус")

    created_date = input("Дата создания заметки: день-месяц-год ")
    issue_date = input("Дата истечения заметки: день-месяц-год ")
    note = {
        "Имя пользователя": username,
        "Заголовок заметки": title,
        "Описание заметки": content,
        "Статус заметки": status,
        "Дата создания заметки": created_date,
        "Дата истечения заметки": issue_date
    }
    notes.append(note)  # добавляем заметку в список
    pprint(note, sort_dicts=False)  # выводим заметку

    note_new = input("Хотите добавить ещё одну заметку да/нет ")
    if note_new.lower() == "нет":
        break
print("Все заметки:")
pprint(notes, sort_dicts=False)












