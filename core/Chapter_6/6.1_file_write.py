def main():
    outfile = open("philosophers.txt", "w")

    outfile.write("Джон Локк\n")
    outfile.write("Дэвид Хьюм\n")
    outfile.write("Эдмунд Берк\n")

    outfile.close()


if __name__ == "__main__":
    main()
