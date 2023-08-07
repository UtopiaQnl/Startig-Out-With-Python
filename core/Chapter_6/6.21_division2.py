def main():
    num1 = int(input("Введите число: "))
    num2 = int(input("Введите число: "))

    if num2 == 0:
        print("Деление на ноль невозможно.")
    else:
        result = num1 / num2
        print(f"{num1} деленное на {num2} равно {result}")


if __name__ == "__main__":
    main()
