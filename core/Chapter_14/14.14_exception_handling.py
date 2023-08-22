import sqlite3


def main():
    again = "y"

    while again == "y":
        item_id = int(input("ID товара: "))
        item_name = input("Название товара: ")
        price = float(input("Цена: "))

        add_item(item_id, item_name, price)

        again = input("Добавить ещё одно позицию? (y/n): ")


def add_item(id, name, price):
    conn = None
    try:
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO Inventory (ItemID, ItemName, Price)
        VALUES (?, ?, ?)
        """, (id, name, price))

        conn.commit()
    except sqlite3.Error as exc:
        print(exc)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    main()
