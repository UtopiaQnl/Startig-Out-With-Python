import bankaccount


def main():
    start_bal = float(input("Введите свой начальный остаток: "))

    savings = bankaccount.BankAccount(start_bal)

    pay = float(input("Сколько выполучили на этой недели: "))
    print("Вношу на счет")
    savings.deposit(pay)

    print(f"Ваш остаток на счете составляет ${savings.get_balance():,.2f}")

    cash = float(input("Какую сумму выжелаете снять co счёта: "))
    print("Снимаю", cash, "деняг")
    savings.withdraw(cash)

    print(f"Ваш остаток на счете составляет ${savings.get_balance():,.2f}")


if __name__ == "__main__":
    main()
