total_summ = 0

print("Введите ряд положительных чисел, а затем отрицательное, чтобы увидеть сумму введённых ранее чисел.")

number = float(input("Введите число: "))

while number >= 0:
    total_summ += number
    number = float(input("Введите число: "))

print(f"Результат сложения: {total_summ}")
