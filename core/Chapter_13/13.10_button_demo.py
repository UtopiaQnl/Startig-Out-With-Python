import tkinter as tk
import tkinter.messagebox


class MyGUI:
    def __init__(self) -> None:
        self.main_window = tk.Tk()

        self.my_button = tk.Button(self.main_window, text="нажми на меня!", command=self.do_something)
        self.my_button.pack()

        tk.mainloop()

    def do_something(self):
        tk.messagebox.showinfo("Заголовок уведомления", "Содержание уведомления")


if __name__ == "__main__":
    MyGUI()
