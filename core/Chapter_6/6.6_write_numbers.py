def main():
    outfile = open("numbers.txt", "w")

    num1 = int(input("Введите число: "))
    num2 = int(input("Введите число: "))
    num3 = int(input("Введите число: "))

    outfile.write(f"{num1}\n")
    outfile.write(f"{num2}\n")
    outfile.write(f"{num3}\n")

    outfile.close()
    print("Данные записаны в numbers.txt")


if __name__ == "__main__":
    main()
