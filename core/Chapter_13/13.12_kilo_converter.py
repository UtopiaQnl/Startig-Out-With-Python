import tkinter as tk
import tkinter.messagebox


class KiloConverterGUI:
    def __init__(self) -> None:
        self.main_window = tk.Tk()

        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        self.prompt_label = tk.Label(self.top_frame, text="Введите расстояние в километрах: ")
        self.kilo_entry = tk.Entry(self.top_frame, width=20)

        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        self.calc_button = tk.Button(self.bottom_frame, text="Преобразовать", command=self.convert)
        self.quit_button = tk.Button(self.bottom_frame, text="Выйти", command=self.main_window.destroy)

        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    def convert(self) -> None:
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        tk.messagebox.showinfo("Результаты", f"{kilo} эквивалентны {miles} милям.")


if __name__ == "__main__":
    KiloConverterGUI()
