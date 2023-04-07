DAYS = 5

total_errors = 0

for day in range(DAYS):
    errors_in_day = int(input(f"Введите кол-во ошибок в день {day + 1}: "))
    total_errors += errors_in_day

print(f"Всегод ошибок за {DAYS} дней - {total_errors}")

