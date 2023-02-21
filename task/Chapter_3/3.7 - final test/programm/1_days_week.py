number_day_week = int(input("Введите число в диапазоне от 1 до 7: "))

MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7

if number_day_week == MONDAY:
    print("Понедельник")
elif number_day_week == TUESDAY:
    print("Вторник")
elif number_day_week == WEDNESDAY:
    print("Среда")
elif number_day_week == THURSDAY:
    print("Четверг")
elif number_day_week == FRIDAY:
    print("Пятнца")
elif number_day_week == SATURDAY:
    print("Суббота")
elif number_day_week == SUNDAY:
    print("Воскресенье")
else:
    print("Ошибка! Вы ввели число вне диапазона от 1-го до 7-ми.")

