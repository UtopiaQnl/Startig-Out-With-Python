ACRE_LAND: float = 4046.86

area = float(input("Введите общее кол-во квадратных метров участка земли: "))

print(f"Кол-во полных акров на участке: {area / ACRE_LAND:.0f}")

