def main():
    emp_file = open("employees.txt")

    name = emp_file.readline()

    while name != "":
        id_num = emp_file.readline().strip()
        dept = emp_file.readline().strip()
        name = name.strip()

        print(f"Имя: {name} ID: {id_num} Отдел: {dept}\n")

        name = emp_file.readline()

    emp_file.close()


if __name__ == "__main__":
    main()
