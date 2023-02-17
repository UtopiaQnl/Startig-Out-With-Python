FEDERAL_ACCOUNT = 0.05
REGIONAL_ACCOUNT  = 0.025

sales = float(input("Введите общую величину покупки: "))

fed_account = sales * FEDERAL_ACCOUNT
reg_account = sales * REGIONAL_ACCOUNT
total_account = fed_account + reg_account
total_summ = sales + total_account

print(f"Общая сумма покупки: ${sales:,.2f}")
print(f"Федеральный налог: ${fed_account:.2f}")
print(f"Региональный налог: ${reg_account:.2f}")
print(f"Общий налог: ${total_account:.2f}")
print(f"Общая сумма продажи: ${total_summ:.2f}")

