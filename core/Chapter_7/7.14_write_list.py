def main():
    cities = ["Нью-Йорк", "Бостон", "Атланта", "Даллас"]
    outfile = open("cities.txt", "w")
    for item in cities:
        outfile.write(item + "\n")
    outfile.close()


if __name__ == "__main__":
    main()
