import sqlite3


def main():
    again = 'y'

    conn = sqlite3.connect("inventory.db")

    cur = conn.cursor()

    while again == 'y':
        item_name = input("Название: ")
        price = float(input("Цена: "))

        cur.execute("""
        INSERT INTO Inventory (ItemName, Price)
        VALUES (?, ?)""", (item_name, price))

        again = input("Добавить ещё одну вещь? ")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
