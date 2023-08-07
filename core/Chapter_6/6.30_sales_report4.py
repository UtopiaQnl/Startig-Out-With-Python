def main():
    total = 0

    try:
        infile = open("sales_data.txt")
        for line in infile:
            amount = float(line)
            total += amount

        infile.close()
    except Exception as err:
        print(err)
    else:
        print(f"{total:,.2f}")


if __name__ == "__main__":
    main()
