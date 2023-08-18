def main():
    number = int(input("Введите неотрицательное целое число: "))
    fact = factorial(number)
    print(f"Факториал числа {number} равняется {fact}.")


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


if __name__ == "__main__":
    main()
