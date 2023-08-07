def main():
    filename = input("Введите название файла: ")
    infile = open(filename)

    contents = infile.read()

    print(contents)

    infile.close()


if __name__ == "__main__":
    main()
