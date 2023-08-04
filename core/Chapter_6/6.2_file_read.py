def main():
    infile = open("philosophers.txt")

    file_countents = infile.read()

    infile.close()

    print(file_countents)


if __name__ == "__main__":
    main()
