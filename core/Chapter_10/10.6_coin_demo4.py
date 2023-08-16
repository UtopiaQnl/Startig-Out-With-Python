import coin


def main():
    my_coin = coin.Coin()
    print("сейчас", my_coin.get_sideup())
    print("10 раз:")
    for _ in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())


if __name__ == "__main__":
    main()
