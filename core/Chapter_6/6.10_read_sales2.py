def main():
    sales_file = open("sales.txt")

    for line in sales_file:
        amount = float(line)
        print(f"{amount:.2f}")

    sales_file.close()


if __name__ == "__main__":
    main()
