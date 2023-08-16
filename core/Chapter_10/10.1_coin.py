import random


class Coin:
    def __init__(self) -> None:
        self.sideup = "Орёл"

    def toss(self) -> None:
        if random.randint(0, 1) == 0:
            self.sideup = "Орёл"
        else:
            self.sideup = "Решка"

    def get_sidup(self) -> str:
        return self.sideup
