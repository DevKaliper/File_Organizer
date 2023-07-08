# This code organizes your files by extension. You just have to choose the path you want to organize and it will do the rest for you.


import os
import shutil

EXTENSIONS = {
    "Fotos": [".jpg", ".png", ".jpeg"],
    "Videos":[".mp4", ".mov", ".avi", ".wav"],
    "Gif":[".gif"],
    "Audio":[".mp3"],
    "PDF": [".pdf"],
    "Office":[ ".dotx", '.xlsx', '.mdb', '.accdb', '.csv', '.pptx', '.docx', ".doc"],
    "Programas":[".exe"],
    "Archivos_para_comprimir": [".rar", ".zip"]

}

#Returns the extension of all files in the path
def get_extentions(path):
    extentions = []
    for iteration in os.listdir(path):
        ext = os.path.splitext(iteration)[1]
        if ext not in extentions and ext != "":
            extentions.append(ext)
    
    return extentions

#Creates the directories
def create_dirs(path):
    extentions = get_extentions(path)
    for dir in EXTENSIONS.keys():
        for file in extentions:
            if file in EXTENSIONS[dir] and not os.path.exists(path+dir):
                os.mkdir(path+dir)
                
        


#Moves the files
def move_files(path, file, ext):
    for dir in EXTENSIONS.keys():
        if ext in EXTENSIONS[dir]:
            try:
                shutil.move(path+file, path+dir)
            except:
                print(f"Esta ruta: {path+file}  dio error al intentar moverla.")

#Main function
def organizer(path):
    create_dirs(path)
    for file in os.listdir(path):
        ext = os.path.splitext(file)[1]
        move_files(path, file, ext)

#The path you want to organize
while True:
    path = input("Dame la ruta la cual quieres organizar: ")
    if os.path.exists(path):
        path+="/"
        break
    
    print("Ruta no encontrada...")

#Runs the program
organizer(path)
print(f"proceso terminado. la ruta es {path} ")


