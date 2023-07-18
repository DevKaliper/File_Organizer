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
                error["text"] = f"Can't move the file: {file}", 



# Main function
def organizer(path):
    create_dirs(path)
    for file in os.listdir(path):
        ext = os.path.splitext(file)[1]
        move_files(path, file, ext)




# The path you want to organize (the user selects the path with a window)
def select_dir():
    path = filedialog.askdirectory()
    if os.path.exists(path):
        path += "/"
        organizer(path)
        error["text"] = f"Process finished, check the path: {path}"
        
    else:
        error["text"] = f"Can't find the path: {path} " 
        

    done["text"] = "Thanks for using the program :)"


root = Tk()
root.title("File organizer Beta 1.0")
root.geometry("600x300")
root.resizable(True, False)
root.config(bg="white")
choose_path = Button(root, text="Choose the path", command=select_dir , cursor="hand2", font=("Arial", 12))
choose_path.pack(pady=20)
error = Label(root, text="", bg="white", fg="red", font=("Arial", 9))
error.pack(pady=20)
done = Label(root, text="", bg="white", fg="green", font=("Arial", 12))
done.pack(pady=20)


root.mainloop()
