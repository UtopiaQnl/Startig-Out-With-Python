import tkinter as tk


class MyGUI:
    def __init__(self) -> None:
        self.main_window = tk.Tk()

        self.label1 = tk.Label(self.main_window, text="Привет мир!", borderwidth=1, relief="solid")
        self.label2 = tk.Label(self.main_window, text="Нормальное длиииииииииииииннное сообщение", borderwidth=1,
                               relief="solid")

        self.label1.pack(ipadx=20, ipady=20)
        self.label2.pack(ipadx=20, ipady=20)

        tk.mainloop()


if __name__ == "__main__":
    MyGUI()
