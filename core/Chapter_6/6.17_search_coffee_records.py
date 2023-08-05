def main():
    found = False
    search = input("Введите искомое описание: ")

    coffee_file = open("coffee.txt")

    desc = coffee_file.readline()

    while desc != "":
        desc = desc.strip()
        count = float(coffee_file.readline())

        if desc == search:
            print(f"Описание: {desc}")
            print(f"Количество: {count}\n")

            found = True

        desc = coffee_file.readline()

    coffee_file.close()

    if not found:
        print("Это значение в файле не найдено.")


if __name__ == "__main__":
    main()
