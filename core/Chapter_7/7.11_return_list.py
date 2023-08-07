def main():
    numbers = get_values()
    print("Числа в списке:")
    print(numbers)


def get_values() -> list[int]:
    values = []
    again = "y"
    while again == "y":
        num = int(input("Введите число: "))
        values.append(num)
        print("Желаете добавить ещё одно число? ")
        again = input("y = yes, else no: ")
        print()

    return values


if __name__ == "__main__":
    main()
