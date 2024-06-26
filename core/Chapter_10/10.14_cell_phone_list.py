import cellphone


def main():
    phones = make_list()
    print("Вот введённые Вами данные:")
    display_list(phones)


def make_list():
    phone_list = []
    print("Введите данные o пяти телефонах:")
    for count in range(1, 6):
        print(f"Номер телефона {count}:")
        man = input("Введите производителя: ")
        mod = input("Введите номер модели: ")
        retail = float(input("Введите розничную цену: "))
        print()

        phone = cellphone.CellPhone(man, mod, retail)
        phone_list.append(phone)

    return phone_list


def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()


if __name__ == "__main__":
    main()
