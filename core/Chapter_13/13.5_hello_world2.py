import tkinter as tk


class MyGUI:
    def __init__(self) -> None:
        self.main_window = tk.Tk()

        self.label1 = tk.Label(self.main_window, text="Привет мир!")
        self.label2 = tk.Label(self.main_window, text="Это я не гей")

        self.label1.pack()
        self.label2.pack()

        tk.mainloop()


if __name__ == "__main__":
    MyGUI()
