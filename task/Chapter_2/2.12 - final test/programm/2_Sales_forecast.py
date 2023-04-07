ANNUAL_PROFIT = 0.23  # Ежегодная прибыль 23% в год

# Ввод плановой суммы общего объема продаж
plan_sales = float(input("Введите плановую сумму общего объема продаж: "))

profit = plan_sales * ANNUAL_PROFIT

# Вывод прибыли
print(f"${profit:,.2f}")

