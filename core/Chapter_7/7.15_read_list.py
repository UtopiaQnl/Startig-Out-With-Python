def main():
    infile = open("cities.txt")
    cities = infile.readlines()
    infile.close()

    index = 0

    while index < len(cities):
        cities[index] = cities[index].rstrip("\n")
        index += 1

    print(cities)


if __name__ == "__main__":
    main()
