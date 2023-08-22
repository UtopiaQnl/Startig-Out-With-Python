import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5


def main():
    choice = 0
    while choice != EXIT:
        display_menu()

        choice = get_menu_choice()

        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()


def display_menu():
    print("\n----- Меню ведения учета инструментов -----")
    print("1. Создать новую позицию")
    print("2. Прочитать позицию")
    print("3. Обновить позицию")
    print("4. Удалить позицию")
    print("5. Выйти из программы")


def get_menu_choice():
    choice = int(input("Введите ваш вариант: "))

    while not (MIN_CHOICE <= choice <= MAX_CHOICE):
        print(f"Допустимые варианты таковы: {MIN_CHOICE} - {MAX_CHOICE}")
        choice = int(input("Введите ваш вариант: "))

    return choice


def create():
    print("Создать новую позицию")
    name = input("Название позиции: ")
    price = input("Цена: ")
    insert_row(name, price)


def read():
    name = input("Введите название искомой позиции: ")
    num_found = display_item(name)
    print(f"{num_found} строк(a) найдено.")


def update():
    read()
    selected_id = int(input("Выберите ID обновляемой позиции: "))
    name = input("Введите новое название позиции: ")
    price = input("Введите новую цену: ")

    num_updated = update_row(selected_id, name, price)
    print(f"{num_updated} строк(a) удалено.")


def delete():
    read()
    selected_id = int(input("Выберите ID удаляемой позиции: "))

    sure = input("Вы уверены, что хотите удалить эту позицию? (y/n): ")
    if sure.lower() == "y":
        num_deleted = delete_row(selected_id)
        print(f"{num_deleted} строк(a) удалено.")


def insert_row(name, price):
    conn = None
    try:
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO Inventory (ItemName, Price)
        VALUES (?, ?)
        """, (name, price))
        conn.commit()

    except sqlite3.Error as exc:
        print("Ошибка базы данных:", exc)
    finally:
        if conn is not None:
            conn.close()


def display_item(name):
    conn = None
    try:
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("""
        SELECT * FROM Inventory
        WHERE ItemName == ?
        """, (name,))
        results = cur.fetchall()

        for row in results:
            print(f"ID: {row[0]:<3} Название: {row[1]:<15} Цена: ${row[2]:<6,.2f}")

    except sqlite3.Error as exc:
        print("Ошибка базы данных:", exc)
    finally:
        if conn is not None:
            conn.close()
        return len(results)


def update_row(id, name, price):
    conn = None
    try:
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("""
        UPDATE Inventory
        SET ItemName = ?, Price = ?
        WHERE ItemID == ?
        """, (id, name, price))
        num_updated = cur.rowcount
    except sqlite3.Error as exc:
        print("Ошибка базы данных:", exc)
    finally:
        if conn is not None:
            conn.close()
        return num_updated


def delete_row(id):
    conn = None
    try:
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("""
        DELETE FROM Inventory
        WHERE ItemId == ?
        """, (id,))
        num_deleted = cur.rowcount
    except sqlite3.Error as exc:
        print("Ошибка базы данных:", exc)
    finally:
        if conn is not None:
            conn.close()
        return num_deleted


if __name__ == "__main__":
    main()
