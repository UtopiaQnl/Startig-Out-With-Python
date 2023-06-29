def main():
    show_interest(rate=0.01, periods=10, principal=10_000.0)


def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print(f"Простой процентный доход составит ${interest:,.2f}")


main()
