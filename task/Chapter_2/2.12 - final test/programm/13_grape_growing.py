R = float(input("Введите длину гряды в метрах: "))
E = float(input("Введите размер пространства в метрах, занимаемого концевыми опорами: "))
S = float(input("Введите расстояние между виноградными лозами в метрах: "))

V = (R - 2 * E) / S

print(f"Кол-во виноградных лоз, которые помястятся на грядке: {V:.0f}")

