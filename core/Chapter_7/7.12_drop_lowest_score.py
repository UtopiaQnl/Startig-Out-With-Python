def main():
    scores = get_scores()
    total = get_total(scores)
    lowest = min(scores)
    total -= lowest
    average = total / (len(scores) - 1)

    print(f"Средняя оценка c учетом отброшенной самой низкой оценки: {average}.")


def get_scores() -> list[float]:
    test_scores = []
    again = "y"
    while again == "y":
        value = float(input("Введите оценку: "))
        test_scores.append(value)
        print("Желаете добавить ещё одно оценку? ")
        again = input("y - yes, else no: ")
        print()
    return test_scores


def get_total(value_list: list[int | float]) -> float:
    total = 0
    for num in value_list:
        total += num
    return total


if __name__ == "__main__":
    main()
