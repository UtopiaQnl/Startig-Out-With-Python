def main():
    infile = open("numbers.txt")

    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    infile.close()

    total = num1 + num2 + num3

    print(f"Числа: {num1}, {num2}, {num3}")
    print(f"Их сумма: {total}")


if __name__ == "__main__":
    main()
