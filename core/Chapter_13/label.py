import tkinter as tk


class MyGUI:
    def __init__(self) -> None:
        self.main_window = tk.Tk()

        for label_name in ("flat", "raised", "sunken", "ridge", "solid", "groove"):
            label = tk.Label(self.main_window, text=label_name, borderwidth=4, relief=label_name)
            label.pack(padx=10, pady=10, ipadx=30, ipady=10)

        tk.mainloop()


if __name__ == "__main__":
    MyGUI()
