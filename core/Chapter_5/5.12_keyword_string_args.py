def main():
    first_name = input("Введите свое имя: ")
    last_name = input("Введите свою фамилию: ")
    print("Ваше имя в обратном порядке")
    reverse_name(last=last_name, first=first_name)


def reverse_name(first, last):
    print(last, first)


main()
