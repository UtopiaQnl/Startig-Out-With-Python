def main():
    filename = input("Введите имя файла: ")

    try:
        infile = open(filename)
        contents = infile.read()
        print(contents)
        infile.close()
    except OSError:
        print("Произошла ошибка при попытке прочитать файл", filename)


if __name__ == "__main__":
    main()
