# Получаем дату от пользователя.
user_month = int(input("Введите номер месяца: "))
user_day = int(input("Введите день месяца: "))
user_year = int(input("Введите двузначный номер года: "))

print(f"Вы ввели дату: {user_day:02}.{user_month:02}.{user_year:02}")

if user_day * user_month == user_year:
    print('Год является магическим.')
else:
    print("Год не является магическим.")

