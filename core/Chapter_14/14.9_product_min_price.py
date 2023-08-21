import sqlite3


def main():
    conn = sqlite3.connect("chocolate.db")

    cur = conn.cursor()

    min_price = float(input("Введите минимальную цену: "))

    cur.execute("""
    SELECT Description, RetailPrice FROM Products
    WHERE
        RetailPrice >= ?
    """, (min_price,))

    results = cur.fetchall()

    if len(results):
        print("Вот результаты:\n")
        print("Oпиcaниe", " " * 27, "Цена")
        print("-" * 41)
        for row in results:
            print(f"{row[0]:35} {row[1]:>5,.2f}")
    else:
        print("Ни одно изделия не найдено.")


if __name__ == "__main__":
    main()
