import sqlite3


def main():
    conn = sqlite3.connect("chocolate.db")

    cur = conn.cursor()

    pid = int(input("Введите ID изделия для ero удаления: "))

    cur.execute("""
    SELECT Description FROM Products
    WHERE ProductID == ?
    """, (pid,))

    results = cur.fetchone()

    if results is not None:
        cur.execute("""
        DELETE FROM Products
        WHERE ProductID == ?
        """, (pid,))
        conn.commit()
        print(f"Изделие было {results[0]} удалено")
    else:
        print(f"ID изделия {pid} не найден.")

    conn.close()


if __name__ == "__main__":
    main()
