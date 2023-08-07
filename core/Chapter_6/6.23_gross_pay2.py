def main():
    try:
        hours = int(input("Сколько часов вы отработали? "))

        pay_rate = float(input("Введите свою почасовую оплату: "))

        gross_pay = hours * pay_rate

        print(f"Заработная плата: ${gross_pay:,.2f}")
    except ValueError:
        print("Ошибка: отработанные часы и почасовая оплата должны быть числами.")


if __name__ == "__main__":
    main()
