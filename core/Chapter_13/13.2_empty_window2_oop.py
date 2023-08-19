import tkinter as tk


class MyGUI:
    def __init__(self) -> None:
        self.__main_window = tk.Tk()
        tk.mainloop()


def main():
    MyGUI()


if __name__ == "__main__":
    main()
