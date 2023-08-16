import random


class Coin:
    def __init__(self) -> None:
        self.__sideup = "Орёл"

    def toss(self) -> None:
        if random.randint(0, 1) == 0:
            self.__sideup = "Орёл"
        else:
            self.__sideup = "Решка"

    def get_sideup(self) -> str:
        return self.__sideup


def main() -> None:
    my_coin = Coin()

    print("Сейчас", my_coin.get_sideup())

    print(10, "раз:")
    for _ in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())


if __name__ == "__main__":
    main()
