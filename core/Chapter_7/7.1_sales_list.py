NUM_DAYS = 5


def main():
    sales = [0] * NUM_DAYS

    for index in range(len(sales)):
        sales[index] = float(input(f"День №{index + 1}: "))

    print("Вот значения, которые были введены: ")
    for value in sales:
        print(value)


if __name__ == "__main__":
    main()
