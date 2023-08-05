def main():
    num_emps = int(input("Сколько записей o сотрудниках вы хотите создать? "))

    emp_file = open("employees.txt", "w")

    for count in range(1, num_emps + 1):
        print(f"Введите данные o сотруднике №{count}")
        name = input("Имя: ")
        id_num = input("Идентификационный номер: ")
        dept = input("Отдел: ")

        emp_file.write(f"{name}\n")
        emp_file.write(f"{id_num}\n")
        emp_file.write(f"{dept}\n")

        print()

    emp_file.close()
    print("Записи o сотрудниках сохранены в employees.txt")


if __name__ == "__main__":
    main()
