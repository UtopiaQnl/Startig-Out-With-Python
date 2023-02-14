# Получить требуемое будущее значение.
future_value = float(input('Введите требуемое будущее значение: '))

# Получить годовую процентную ставку.
rate = float(input('Введите годовую процентную ставку: '))

# Получить количество лет хранения денег на счете.
years = int(input('Введите количество лет хранения денег на счете: '))

# Рассчитать сумму, необходимую для внесения на счет.
present_value = future_value / (1.0 + rate) ** years

# Показать сумму, необходимую для внесения на счет.
print('Вам потребуется внести сумму:', present_value)
