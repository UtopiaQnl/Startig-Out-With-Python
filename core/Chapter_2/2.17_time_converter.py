# Получить от пользователя количество секунд.
total_seconds = float(input('Введите количество секунд: '))

# Получить количество часов/
hours = total_seconds // 3600

# Получить количество оставшихся минут.
minutes = (total_seconds // 60) % 60

# Получить количество оставшихся секунд.
seconds = total_seconds % 60

# Показать результаты.
print('Вот время в часах, минутах и секундах:')
print('Часы:', hours)
print('Минуты:', minutes)
print('Секунды:', seconds)
