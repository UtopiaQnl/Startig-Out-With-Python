def main():
    num1 = int(input("Введите целое число: "))
    num2 = int(input("Введите ещё одно целое число: "))

    print(f"Наибольший общий делитель для {num1} и {num2} равняется {gcd(num1, num2)}")


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


if __name__ == "__main__":
    main()
