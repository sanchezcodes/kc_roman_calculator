import tkinter as tk
from calc.views import CalcButton, KeyBoard, Display, Calculator

# hay que crear los estados de la aplicación
# EMPTY, PARTIAL, PENDING, COMPLETE, SHOWN


def fn1(cad):
    print(f"has llamado a f1 con {cad}")
    calc.show(cad)


root = tk.Tk()
root.pack_propagate(True)

calc = Calculator(root, fn1)
calc.pack()

root.mainloop()
