import cellphone


def main():
    man = input("Введите производителя: ")
    mod = input("Введите номер модели: ")
    retail = float(input("Введите розничную цену: "))

    phone = cellphone.CellPhone(man, mod, retail)

    print("Вот введённые Вами дaнныe:")
    print(f"Производитель: {phone.get_manufact()}")
    print(f"Номер модели: {phone.get_model()}")
    print(f"Розничная цена: {phone.get_retail_price()}")


if __name__ == "__main__":
    main()
