import tkinter as tk
import tkinter.messagebox


class MyGUI:
    def __init__(self) -> None:
        self.main_window = tk.Tk()
        self.my_button = tk.Button(self.main_window, text="Нажми на меня", command=self.do_something)
        self.quit_button = tk.Button(self.main_window, text="выйти", command=self.main_window.destroy)

        self.my_button.pack()
        self.quit_button.pack()

        tk.mainloop()

    def do_something(self) -> None:
        tk.messagebox.showinfo("Реакция", "Благодарю, что нажали на кнопку.")


if __name__ == "__main__":
    MyGUI()
