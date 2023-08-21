import sqlite3


def fetchall(func):
    def inner(*args, agr_func=False):
        results = func(*args)
        if agr_func is True:
            return results[0][0]
        return results

    return inner


def main():
    conn = sqlite3.connect("chocolate.db")

    cur = conn.cursor()


    cur.execute("""
    SELECT MIN(RetailPrice) FROM Products
    """)
    lowest = cur.fetchone()[0]

    cur.execute("""
    SELECT MAX(RetailPrice) FROM Products
    """)
    highest = cur.fetchone()[0]

    cur.execute("""
    SELECT AVG(RetailPrice) FROM Products
    """)

    fetch = fetchall(cur.fetchall)

    print(f"Минимальная цена: ${lowest:<5,.2f}")
    print(f"Максимальная цена: ${highest:<5,.2f}")
    print(f"Средняя цена: ${fetch(agr_func=True):<5,.2f}")

    conn.close()


if __name__ == "__main__":
    main()
