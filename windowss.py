from tkinter import *
from tkinter import ttk
import os


def pathFinder(path):
    if os.path.exists(path):
        print(f"Ruta encontrada: {path} ")
    else:
        print(f"No he podido encontrar la ruta: {path}")


root = Tk()
root.title("Probando ttk")


root.geometry("300x200")
entry = ttk.Entry()

entry.place(x=50, y=50)
label = ttk.Label(text="Hola mundo")
label.place(x=50, y=150)

button = ttk.Button(text="Coloca la ruta a organizar",
                    command=lambda: pathFinder(entry.get()))
button.place(x=50, y=100)
root.mainloop()
