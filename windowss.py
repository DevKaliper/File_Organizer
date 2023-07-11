from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Probando ttk")
root.geometry("300x200")
entry = ttk.Entry()
entry.insert(0, "Hola test")
entry.place(x=50, y=50)
button = ttk.Button(text="Obtener texto", command=lambda: print(entry.get()))
button.place(x=50, y=100)
root.mainloop()