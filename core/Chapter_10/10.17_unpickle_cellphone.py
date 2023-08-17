import pickle

import cellphone

FILENAME = "cellphone.dat"


def main():
    end_of_file = False

    input_file = open(FILENAME, "rb")

    while not end_of_file:
        try:
            phone = pickle.load(input_file)
            display(phone)
        except EOFError:
            end_of_file = True

    input_file.close()


def display(phone: cellphone.CellPhone):
    print(f"Производитель: {phone.get_manufact()}")
    print(f"Модель: {phone.get_model()}")
    print(f"Цена: {phone.get_retail_price()}\n")


if __name__ == "__main__":
    main()
