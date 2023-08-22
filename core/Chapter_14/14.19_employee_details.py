import sqlite3
import tkinter as tk
import tkinter.messagebox


class EmployeeDetails:
    def __init__(self) -> None:
        self.main_window = tk.Tk()
        self.__build_main_window()
        tk.mainloop()

    def __build_main_window(self):
        self.__create_prompt_label()
        self.__build_listbox_frame()
        self.__create_quit_button()

    def __create_prompt_label(self):
        self.employee_prompt_label = tk.Label(self.main_window, text="Выберите сотрудника")
        self.employee_prompt_label.pack(side="top", padx=5, pady=5)

    def __build_listbox_frame(self):
        self.listbox_frame = tk.Frame(self.main_window)
        self.__setup_listbox()
        self.__create_scrollbar()
        self.__populate_listbox()
        self.listbox_frame.pack()

    def __setup_listbox(self):
        self.employee_listbox = tk.Listbox(self.listbox_frame, selectmode=tk.SINGLE, height=6)
        self.employee_listbox.bind("<<ListboxSelect>>", self.__get_details)
        self.employee_listbox.pack(side="left", padx=5, pady=5)

    def __create_scrollbar(self):
        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.employee_listbox.yview)
        self.employee_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill=tk.Y)

    def __populate_listbox(self):
        for emp in self.__get_employees():
            self.employee_listbox.insert(tk.END, emp)

    def __create_quit_button(self):
        self.quit_button = tk.Button(self.main_window, text="Выйти", command=self.main_window.destroy)
        self.quit_button.pack(side="top", padx=10, pady=5)

    def __get_employees(self):
        employee_list = []
        conn = None
        try:
            conn = sqlite3.connect("employees.db")
            cur = conn.cursor()
            cur.execute("""SELECT Name FROM Employees""")

            employee_list = [n[0] for n in cur.fetchall()]
        except sqlite3.Error as exc:
            tk.messagebox.showerror("ошибка базы данных", f"{exc}")
        finally:
            if conn is not None:
                conn.close()
            return employee_list

    def __get_details(self, event):
        listbox_index = self.employee_listbox.curselection()[0]
        selected_emp = self.employee_listbox.get(listbox_index)

        conn = None
        try:
            conn = sqlite3.connect("employees.db")
            cur = conn.cursor()
            cur.execute("""
            SELECT
                Employees.Name,
                Employees.Position,
                Departments.DepartmentName,
                Locations.City
            FROM
                Employees, Departments, Locations
            WHERE
                Employees.Name = ?
                AND
                Employees.DepartmentID == Departments.DepartmentID
                AND
                Employees.LocationID == Locations.LocationID
            """, (selected_emp,))
            results = cur.fetchone()
            self.__display_details(name=results[0], position=results[1], department=results[2], location=results[3])
        except sqlite3.Error as exc:
            tk.messagebox.showerror("ошибка БАзы данных", f"{exc}")
        finally:
            if conn is not None:
                conn.close()

    def __display_details(self, name, position, department, location):
        tk.messagebox.showinfo("Информация o сотруднике", f"Имя: {name}"
                                                          f"\nДoлжнocть: {position}"
                                                          f"\nOтдeл: {department}"
                                                          f"\nMecтoпoлoжeниe: {location}")


if __name__ == "__main__":
    EmployeeDetails()
