CONTRIBUTION_RATE = 0.05


def main():
    gross_pay = float(input("Введите заработную плату: "))
    bonus = float(input("Введите сумму премий: "))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)


def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print(f"Взнос исходя из заработнйо платы: ${contrib:,.2f}.")


def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print(f"Взнос исходя из суммы премии: ${contrib:,.2f}.")


main()
