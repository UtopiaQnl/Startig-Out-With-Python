user_number = int(input("Введите число от 0-ля до 36-ти: "))

if not (user_number <= 0 and user_number <= 36):
    print("Ошибка! Вы ввели число не в диапазоне от 0-36")

if user_number == 0:
    print("ВЕЗЁТ, ЗЕЛЕНЫЙ!")
elif 1 <= user_number and user_number <= 10:
    if user_number % 2 == 0:
        print("Черный")
    else:
        print("Красный")
elif 11 <= user_number and user_number <= 18:
    if user_number % 2 == 0:
        print("Красный")
    else:
        print("Черный")
elif 19 <= user_number and user_number <= 28:
    if user_number % 2 == 0:
        print("Черный")
    else:
        print("Красный")
elif 29 <= user_number and user_number <= 36:
    if user_number % 2 == 0:
        print("Красный")
    else:
        print("Черный")
