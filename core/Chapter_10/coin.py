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
