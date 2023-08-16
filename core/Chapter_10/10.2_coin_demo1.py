import random


class Coin:
    def __init__(self) -> None:
        self.sideup = "Орёл"

    def toss(self) -> None:
        if random.randint(0, 1) == 0:
            self.sideup = "Орёл"
        else:
            self.sideup = "Решка"

    def get_sideup(self) -> str:
        return self.sideup


def main() -> None:
    my_coin = Coin()

    print("Эта сторона обращена вверх:", my_coin.get_sideup())

    print("Подбрасываем монету...")
    my_coin.toss()

    print("Эта сторона обращена вверх:", my_coin.get_sideup())


if __name__ == "__main__":
    main()
