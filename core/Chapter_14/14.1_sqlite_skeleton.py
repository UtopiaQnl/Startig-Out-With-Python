import sqlite3


def main():
    conn = sqlite3.connect("contacts.db")
    conn.cursor()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
