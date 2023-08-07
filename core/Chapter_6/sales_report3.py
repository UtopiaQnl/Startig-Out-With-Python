def main():
    total = 0

    try:
        infile = open("sales_data.txt")
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
        print(f"{total:,.2f}")
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    main()
