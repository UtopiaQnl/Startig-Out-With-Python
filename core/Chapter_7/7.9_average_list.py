def main():
    scores = [2.5, 7.3, 6.5, 4.0, 5.2]
    total = 0
    for value in scores:
        total += value

    average = total / len(scores)

    print(f"Среднее значение элементов составляет: {average}.")


if __name__ == "__main__":
    main()
