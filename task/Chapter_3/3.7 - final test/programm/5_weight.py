user_weight = float(input("Введите вашу массу тела: "))

G = 9.8

weight_h = user_weight * G

if weight_h > 500:
    print("Ваше тело слишком тяжелое.")
elif weight_h < 100:
    print("Ваше тело слишком легкое.")
else:
    print(f"Вес вашего тела равен: {weight_h:,.2f}H")
