# Эта программа предсказывает приблизительный размер популяции организмов.

start_count_entity = int(input("Введите стартовое кол-во организмов: "))
average_daily_increase = int(input("Введите среднесуточное увеличение в процентах: ")) / 100
num_days_for_reproduction = int(input("Введите кол-во дней для размножения: "))

print("День\tПопуляция")

total = start_count_entity
for day in range(num_days_for_reproduction):
    print(f"{day+1}\t{total:,.3f}")

    total *= (1 + average_daily_increase)
