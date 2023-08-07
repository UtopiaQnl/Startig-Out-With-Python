def main():
    name_list = []

    again = "Y"

    while again == "Y":
        name = input("Введите имя: ")
        name_list.append(name)
        print("Желаете добавить ещё одно имя?")
        again = input("Y = yes, else no: ")
        print()

    print("Вот имена, которые были введены.")

    for name in name_list:
        print(name)


if __name__ == "__main__":
    main()
