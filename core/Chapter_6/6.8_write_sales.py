def main():
    num_days = int(input("3a какое количество дней вы располагаете продажами? "))

    sales_file = open("sales.txt", "w")

    for count in range(1, num_days + 1):
        sales = float(input(f"Введите продажи на день №{count}: "))
        sales_file.write(f"{sales}\n")

    sales_file.close()
    print("Данные записаны в sales.txt")


if __name__ == "__main__":
    main()
