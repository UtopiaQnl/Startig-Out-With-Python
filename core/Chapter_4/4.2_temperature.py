# Эта программа помогает лаборанту в процессе
# контроля температуры вещества.

# Именованная константа, которая представляет максимальную
# темпуратуры вещества.
MAX_TEMP = 102.5

# Получить температуру вещества.
temperature = float(input("Введите температуру вещества в градусах Цельсия: "))

# Пока есть необходимость, инструктировать пользователя
# в корректировке нагрева.
while temperature > MAX_TEMP:
    print("Температура слишком высока")
    print("Убавьте нагрев и подожите")
    print("5 минут. Затем снимите показания температуры")
    print("снова и введите полученное значение.")
    temperature = float(input("Введите новое значение температуры: "))
