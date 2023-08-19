import tkinter as tk


class MyGUI:
    def __init__(self) -> None:
        self.main_window = tk.Tk()

        self.label1 = tk.Label(self.main_window, text="Привет мир", borderwidth=1, relief="solid")
        self.label2 = tk.Label(self.main_window, text="Оччч длиииииииинный текст", borderwidth=1, relief="solid")

        self.label1.pack(padx=(130, 5), pady=(20, 10))  # padx = (слева, справа)
        self.label2.pack(padx=(20, 50), pady=100, ipadx=40, ipady=10)  # pady = (сверху, снизу)

        # Это работает только c внешним отступом!

        tk.mainloop()


if __name__ == "__main__":
    MyGUI()
