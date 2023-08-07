def main():
    total = 0

    try:
        infile = open("sales.txt")

        for line in infile:
            amount = float(line)
            total += amount

        infile.close()

        print(f"{total:,.2f}")
    except:
        print("Произошла ошибка")


if __name__ == "__main__":
    main()
