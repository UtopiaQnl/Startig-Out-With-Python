def main():
    first_age = int(input('Введите свой возраст: '))
    second_age = int(input('Введите возраст своего лучшего друга: '))
    total = sum(first_age, second_age)
    print(f"Вместе вам {total} лет.")


def sum(num1, num2):
    result = num1 + num2
    return result


main()
