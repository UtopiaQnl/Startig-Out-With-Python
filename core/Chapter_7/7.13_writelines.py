def main():
    cities = ["Нью-Йорк", "Бостон", "Атланта", "Даллас"]
    outfile = open("cities.txt", "w")
    outfile.writelines(cities)
    outfile.close()


if __name__ == "__main__":
    main()
