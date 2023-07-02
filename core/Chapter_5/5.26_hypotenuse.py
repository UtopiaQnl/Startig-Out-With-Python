import math


def main():
    a = float(input('Введите длину стороны A:'))
    b = float(input('Введите длину стороны B:'))

    c = math.hypot(a, b)

    print(f"Длина гипотенузы составляет {c}.")


main()
