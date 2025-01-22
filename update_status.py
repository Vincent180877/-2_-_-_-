status = input("Статус заметки ")
status_ = {"Текущий статус заметки " : status}
print(status_)
while True:
    status = input("Выберите новый статус заметки  1:выполнено, 2:в процессе, 3:отложено ")
    if status == "1" or status == "выполнено":
        print("Текущий статус заметки: Выполнено")
        break
    elif status == "2" or status == "в процессе":
        print("Текущий статус заметки: В процессе")
        break
    elif status == "3" or status == "отложено":
        print("Текущий статус заметки: Отложено")
        break
    else:
        print("Некорректно введен статус")