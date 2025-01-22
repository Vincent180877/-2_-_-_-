import datetime

print("Текущая дата: " , datetime.datetime.today().strftime("%d.%m.%Y"))
while True:
    issue_date = input("Дата истечения заметки:день.месяц.год ")
    try:
        issue_date = datetime.datetime.strptime(issue_date, '%d.%m.%Y')
        break
    except ValueError:
        print("Неверный ввод даты")
        print("Введите дату ещё раз")
my_date = datetime.datetime.today()
days = (issue_date -my_date).days
if days < 0:
    print("Дедлайн истек", -days, " дней назад")
else:
    print("До дедлайна осталось", days, "дней")
