def main():
    count = 0

    my_string = input("Введите предложение: ")

    for ch in my_string:
        if ch == "T" or ch == "т":
            count += 1

    print(f"Буква T появляется {count} раз(a).")


if __name__ == "__main__":
    main()
