import tkinter as tk


class TestAVG:
    def __init__(self) -> None:
        self.main_window = tk.Tk()

        self.test1_frame = tk.Frame(self.main_window)
        self.test2_frame = tk.Frame(self.main_window)
        self.test3_frame = tk.Frame(self.main_window)
        self.avg_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)

        self.test1_label = tk.Label(self.test1_frame, text="Введите оценку 1:")
        self.test1_entry = tk.Entry(self.test1_label, width=10)
        self.test1_label.pack(side='right')
        self.test1_entry.pack(side='left')

        self.test2_label = tk.Label(self.test2_frame, text="Введите оценку 2:")
        self.test2_entry = tk.Entry(self.test2_label, width=10)
        self.test2_label.pack(side="left")
        self.test2_entry.pack(side="left")


        self.test3_label = tk.Label(self.test3_frame, text="Введите оценку 3:")
        self.test3_entry = tk.Entry(self.test3_label, width=10)
        self.test3_label.pack(side="left")
        self.test3_entry.pack(side="left")

        self.result_label = tk.Label(self.avg_frame, text="Средний балл:")
        self.avg = tk.StringVar()
        self.avg_label = tk.Label(self.avg_frame, textvariable=self.avg)
        self.result_label.pack(side="left")
        self.avg_label.pack(side="left")

        self.calc_button = tk.Button(self.button_frame, text="Усреднить", command=self.calc_avg)
        self.quit_button = tk.Button(self.button_frame, text="Выйти", command=self.main_window.destroy)

        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        tk.mainloop()

    def calc_avg(self) -> None:
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())

        self.average = (self.test1 + self.test2 + self.test3) / 3

        self.avg.set(self.average)


if __name__ == "__main__":
    TestAVG()
