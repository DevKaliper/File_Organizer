from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import shutil
EXTENSIONS = {
    "Fotos": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".mov", ".avi", ".wav"],
    "Gif": [".gif"],
    "Audio": [".mp3"],
    "PDF": [".pdf"],
    "Office": [".dotx", '.xlsx', '.mdb', '.accdb', '.csv', '.pptx', '.docx', ".doc"],
    "Programas": [".exe"],
    "Archivos_para_comprimir": [".rar", ".zip"]

}


# Returns the extension of all files in the path
def get_extentions(path):
    extentions = []
    for iteration in os.listdir(path):
        ext = os.path.splitext(iteration)[1]
        if ext not in extentions and ext != "":
            extentions.append(ext)

    return extentions

# Creates the directories


def create_dirs(path):
    extentions = get_extentions(path)
    for dir in EXTENSIONS.keys():
        for file in extentions:
            if file in EXTENSIONS[dir] and not os.path.exists(path+dir):
                os.mkdir(path+dir)

# Moves the files


def move_files(path, file, ext):
    for dir in EXTENSIONS.keys():
        if ext in EXTENSIONS[dir]:
            try:
                shutil.move(path+file, path+dir)
            except:
                print(
                    f"Esta ruta: {path+file}  dio error al intentar moverla.")



# Main function
def organizer(path):
    create_dirs(path)
    for file in os.listdir(path):
        ext = os.path.splitext(file)[1]
        move_files(path, file, ext)


# The path you want to organize
def pathFinder(path):

    if os.path.exists(path):
        path += "/"
        organizer(path)
        print("Process finished, check the path: ", path)

    else:
        print("Can't find the path: ", path)


# The path you want to organize (the user selects the path with a window)
def select_dir():
    path = filedialog.askdirectory()
    if os.path.exists(path):
        path += "/"
        organizer(path)
        print("Process finished, check the path: ", path)
    else:
        print("Can't find the path: ", path)

    print("Process finished")


root = Tk()
root.title("Probando ttk")


root.geometry("300x200")
entry = ttk.Entry()

entry.place(x=100, y=50)
button = ttk.Button(text="Seleciona directorio",
                    command=select_dir).place(x=100, y=150)


button = ttk.Button(text="Coloca la ruta a organizar",
                    command=lambda: pathFinder(entry.get()))
button.place(x=90, y=100)
root.mainloop()
