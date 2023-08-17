import pickle

import cellphone

FILENAME = "cellphone.dat"


def main():
    again = "y"

    output_file = open(FILENAME, "wb")

    while again.lower() == "y":
        man = input("Введите производителя: ")
        mod = input("Введите номер модели: ")
        retail = float(input("Введите розничную цену: "))

        phone = cellphone.CellPhone(man, mod, retail)

        pickle.dump(phone, output_file)

        again = input("Введите еще один элемент данных? ")

    output_file.close()
    print(f"Данные записаны в {FILENAME}")


if __name__ == "__main__":
    main()
