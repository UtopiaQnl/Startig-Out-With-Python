import random

MIN = 1
MAX = 6


def main():
    again = 'y'

    while again == 'y' or again == 'Y':
        print("Бросаем кубики...")
        print("Значение граней:")
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        again = input("Бросить кубики ещё раз? (y = да): ")


main()
