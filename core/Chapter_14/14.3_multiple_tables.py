import sqlite3


def main():
    conn = sqlite3.connect("company.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INTEGER PRIMARY KEY NOT NULL,
        Name TEXT,
        Email TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INTEGER PRIMARY KEY NOT NULL,
        Name TEXT,
        Position TEXT
    )
    """)

    cur.execute("""
    DROP TABLE IF EXISTS Customers
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
