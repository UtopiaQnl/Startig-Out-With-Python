import bankaccount2


def main():
    start_bal = float(input("Введите свой начальный остаток: "))
    save = bankaccount2.BackAccount(start_bal)

    pay = float(input("Сколько выполучили на этой недели: "))
    print("Вношу на счет")
    save.deposit(pay)

    print(save)

    cash = float(input("Какую сумму выжелаете снять co счёта: "))
    print("Снимаю", cash, "деняг")
    save.withdraw(cash)

    print(save)


if __name__ == "__main__":
    main()
