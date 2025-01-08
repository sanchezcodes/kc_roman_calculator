import tkinter as tk
from calc.views import CalcButton, KeyBoard, Display, Calculator


def fn1(cad):
    print(f"has llamado a f1 con {cad}")
    calc.show(cad)

root = tk.Tk()
root.pack_propagate(True)

calc = Calculator(root, fn1)
calc.pack()

root.mainloop()