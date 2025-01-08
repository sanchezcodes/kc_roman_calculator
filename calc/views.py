import tkinter as tk
from typing import Callable

BUTTON_WIDTH = 90
BUTTON_HEIGHT = 50


class CalcButton(tk.Frame):
    def __init__(self, root, text: str, command: Callable):
        super().__init__(root, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        self.pack_propagate(False)
        btn = tk.Button(self, text=text, command=self.handle_click)
        btn.pack(expand=True, side=tk.TOP, fill=tk.BOTH)

        self.text = text
        self.command = command

    def handle_click(self):
        self.command(self.text)


class KeyBoard(tk.Frame):
    def __init__(self, root, command: Callable):
        super().__init__(root, width=3 * BUTTON_WIDTH, height=5 * BUTTON_HEIGHT)
        self.grid_propagate(False)

        self.buttons = []
        text_buttons = ("clear", "%", "/",
                        "I", "V", "*",
                        "X", "L", "-",
                        "C", "D", "+",
                        "M", "•", "=")

        for i in range(5):
            for j in range(3):
                index = i * 3 + j
                if index < len(text_buttons):  # Check if the index is within bounds
                    btn = CalcButton(self, text=text_buttons[index], command=command)
                    btn.grid(row=i, column=j, sticky=tk.NSEW)
                    self.buttons.append(btn)


class Display(tk.Frame):
    def __init__(self, parent, text: str = "0"):
        super().__init__(parent, width=(BUTTON_WIDTH * 3), height=BUTTON_HEIGHT)
        self.pack_propagate(False)
        self.lbl_display = tk.Label(self, text=text, fg="white", bg="black", anchor=tk.E, font=("Arial", 36))
        self.lbl_display.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    def show(self, text: str):
        self.lbl_display.config(text=text)


class Calculator(tk.Frame):
    def __init__(self, parent, command: Callable):
        super().__init__(parent)
        self.pack(expand=True, fill=tk.BOTH)

        self.display = Display(self)
        self.display.pack()

        key_board = KeyBoard(self, command)
        key_board.pack()

    def show(self, text: str):
        self.display.show(text)
