def main():
    prod_nums = ["V475", "F987", "Q143", "R688"]
    search = input("Введите номер изделия: ")
    if search in prod_nums:
        print(f"{search} найден в списке.")
    else:
        print(f"{search} не найден в списке.")


if __name__ == "__main__":
    main()
