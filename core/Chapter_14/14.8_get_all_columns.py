import sqlite3


def main():
    conn = sqlite3.connect("employees.db")

    cur = conn.cursor()


    cur.execute("""
    SELECT City FROM Locations
    """)

    results = cur.fetchall()

    for row in results:
        print(*row)

    conn.close()


if __name__ == "__main__":
    main()
