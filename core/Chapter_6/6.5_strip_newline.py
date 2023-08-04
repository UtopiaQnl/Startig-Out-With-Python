def main():
    infile = open("philosophers.txt")

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    line1 = line1.rstrip("\n")
    line2 = line2.rstrip("\n")
    line3 = line3.rstrip("\n")

    infile.close()

    print(line1, line2, line3, sep="\n")


if __name__ == "__main__":
    main()
