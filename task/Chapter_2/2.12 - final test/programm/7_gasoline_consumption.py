distance = float(input("Введите пройденное расстояние в километрах: "))
gasoline_consumption = float(input("Введите расход бензина: "))

result = distance / gasoline_consumption

print(f"Расход бензина на километры пройденного пути: {result:,.2f}")

