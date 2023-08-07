def main():
    food = ["Пицца", "Бургеры", "Чипсы"]
    print("Вот значения списка продуктов питания:")
    print(food)
    item = input("Какое значение следует удалить? ")

    try:
        food.remove(item)
        print("Вот пересмотренный список:")
        print(food)
    except ValueError:
        print("Это значение в списке не найдено.")


if __name__ == "__main__":
    main()
