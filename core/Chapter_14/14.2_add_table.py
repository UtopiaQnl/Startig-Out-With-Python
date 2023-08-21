import sqlite3


def main():
    conn = sqlite3.connect("inventory.db")

    cur = conn.cursor()

    cur.execute("""CREATE TABLE Inventory (ItemID INTEGER PRIMARY KEY NOT NULL,
                                            ItemName TEXT,
                                            Price REAL)""")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
