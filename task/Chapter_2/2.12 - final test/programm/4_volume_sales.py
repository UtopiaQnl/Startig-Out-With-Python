ACCOUNT = 0.07

good_1 = float(input("Введите цену для товара №1: "))
good_2 = float(input("Введите цену для товара №2: "))
good_3 = float(input("Введите цену для товара №3: "))
good_4 = float(input("Введите цену для товара №4: "))
good_5 = float(input("Введите цену для товара №5: "))

total_summ = good_1 + good_2 + good_3 + good_4 + good_5
account_summ = total_summ * ACCOUNT
result_summ = total_summ - account_summ

print(
    f"Накопленная сумма: ${total_summ:,.2f}\n"
    f"Сумма налога {ACCOUNT:.2%}: ${account_summ:,.2f}\n"
    f"Итоговая сумма: ${result_summ:,.2f}\n"
)

