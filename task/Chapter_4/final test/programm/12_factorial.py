n = int(input("Введите целое не отрицательное число от 1: "))

while n <= 0:
    print("Ошибка! Вы ввели отрицательное значение или ноль. Повторите попытку.")
    n = int(input("Введите целое не отрицательное число от 1: "))

result = 1

for x in range(1, n + 1):
    result *= x

print(f"Результат факториала числа {n} равен - {result}")

