def main():
    intro()
    cups_needed = int(input("Введите число чашек: "))
    cups_to_ounces(cups_needed)


def intro():
    print("Эта программа конвертирует замеры")
    print("в чашках в жидкие унции. Для")
    print("справки приводим формулу:")
    print(" 1 чашка = 8 жидких ункций")
    print()


def cups_to_ounces(cups):
    ounces = cups * 8
    print(f"Это число конвертируется в {ounces} унции(й).")


main()
