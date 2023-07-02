def main():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    comm_rate = determine_comm_rate(sales)
    pay = sales * comm_rate - advanced_pay
    print(f"Выплата составляет ${pay:,.2f}.")

    if pay < 0:
        print('Продавец должен возместить разницу компании.')


def get_sales():
    monthly_sales = float(input('Введите сумму месячных продаж: '))
    return monthly_sales


def get_advanced_pay():
    print('Введите сумму авансовой выплаты либо')
    print('введите 0, если такой выплаты не было.')
    advanced = float(input('Авансовая выплата: '))
    return advanced


def determine_comm_rate(sales):
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18
    return rate


main()
