def main():
    value = 99
    print(f"Значение равно {value = }")
    change_me(value)
    print(f"Теперь значение равно {value = }")


def change_me(arg):
    print("Я измению значение.")
    arg = 0
    print(f"Теперь значение равно {arg = }")


main()
