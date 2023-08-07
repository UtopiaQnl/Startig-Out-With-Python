def main():
    infile = open("numberlist.txt")

    numbers = infile.readlines()

    infile.close()

    for idx in range(len(numbers)):
        numbers[idx] = int(numbers[idx])

    print(numbers)


if __name__ == "__main__":
    main()
