def main():
    another = "y"
    coffee_file = open("coffee.txt", "a")

    while another == "y" or another == "Y":
        print("Введите следующие данные o кофе:")
        desc = input("Описание: ")
        count = int(input("Количество (в фунтах): "))

        coffee_file.write(f"{desc}\n")
        coffee_file.write(f"{count}\n")

        print("Желаете ли вы добавить ещё одну запись?")
        another = input("Y = yes, все остальное = no: ")

    coffee_file.close()
    print("Данные сохранены в coffee.txt")


if __name__ == "__main__":
    main()
