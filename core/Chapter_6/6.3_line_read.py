def main():
    infile = open("philosophers.txt")

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    infile.close()

    print(line1, line2, line3, sep="\n")


if __name__ == "__main__":
    main()
