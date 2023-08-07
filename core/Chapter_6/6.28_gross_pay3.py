def main():
    try:
        hours = int(input("Сколько часов вы отработали? "))

        pay_rate = float(input("Введите почасовую ставку: "))

        gross_pay = hours * pay_rate

        print(f"Зарплата: ${gross_pay:,.2f}")
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()
