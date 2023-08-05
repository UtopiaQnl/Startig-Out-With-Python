from pathlib import Path


def main():
    found = False
    search = input("Введите искомое описание: ")
    new_count = int(input("Введите новое количество: "))

    coffee_file = open("coffee.txt")

    temp_file = open("temp.txt", "w")

    desc = coffee_file.readline()

    while desc != "":
        count = float(coffee_file.readline())
        desc = desc.strip()

        temp_file.write(f"{desc}\n")

        if desc == search:
            temp_file.write(f"{new_count}\n")
            found = True
        else:
            temp_file.write(f"{count}\n")

        desc = coffee_file.readline()

    coffee_file.close()
    temp_file.close()

    Path("coffee.txt").unlink()
    Path("temp.txt").rename("coffee.txt")

    if found is True:
        print("Файл обновлен.")
    else:
        print("Это значение в файле не найдено.")


if __name__ == "__main__":
    main()
