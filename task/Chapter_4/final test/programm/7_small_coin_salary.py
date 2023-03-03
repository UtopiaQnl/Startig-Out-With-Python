total_money_value = 1  # Копеек


number_days = int(input('Введите кол-во дней удвоения: '))
for day in range(number_days):
    total_money_value *= 2

result = total_money_value / 100
print(f"Результат: {result:,.2f}р")

