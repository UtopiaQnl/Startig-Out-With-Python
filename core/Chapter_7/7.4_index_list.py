def main():
    food = ["Пицца", "Бургеры", "Чипсы"]
    print("Вот значения списка продуктов питания:")
    print(food)
    item = input("Какое значение следует изменить? ")
    try:
        item_index = food.index(item)
        new_item = input("Введите новое значение: ")
        food[item_index] = new_item
        print("Вот пересмотренный список:")
        print(food)
    except ValueError:
        print("Это значение в списке не найдено.")


if __name__ == "__main__":
    main()
