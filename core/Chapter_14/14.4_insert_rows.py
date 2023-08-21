import sqlite3


def main():
    conn = sqlite3.connect("inventory.db")

    cur = conn.cursor()

    cur.execute("""
    INSERT INTO Inventory (ItemName, Price)
    VALUES ("Отвертка", 4.99)
    """)

    cur.execute("""
    INSERT INTO Inventory (Price, ItemName)
    VALUES (12.99, "Молоток")
    """)

    cur.execute("""
    INSERT INTO Inventory (ItemName, Price)
    VALUES ("Плоскогубцы", 14.99)
    """)

    cur.execute("""
    INSERT INTO Inventory (ItemName, Price)
    VALUES  ("дрель", NULL)
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
