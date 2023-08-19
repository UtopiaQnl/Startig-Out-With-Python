import tkinter as tk


class MyGUI:
    def __init__(self) -> None:
        self.main_window = tk.Tk()

        self.top_frame = tk.Frame(self.main_window, borderwidth=1, relief="solid")
        self.bottom_frame = tk.Frame(self.main_window, borderwidth=1, relief="solid")

        self.label1 = tk.Label(self.top_frame, text="Мигнуть")
        self.label2 = tk.Label(self.top_frame, text="Моргнуть")
        self.label3 = tk.Label(self.top_frame, text="Кивнуть")

        self.label1.pack(side="top")
        self.label2.pack(side="top")
        self.label3.pack(side="top")

        self.label4 = tk.Label(self.bottom_frame, text="Мигнуть")
        self.label5 = tk.Label(self.bottom_frame, text="Моргнуть")
        self.label6 = tk.Label(self.bottom_frame, text="Кивнуть")

        self.label4.pack(side="left")
        self.label5.pack(side="left")
        self.label6.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop()


if __name__ == "__main__":
    MyGUI()
