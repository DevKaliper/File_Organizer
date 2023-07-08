import os
import shutil
import ctypes
from ctypes import wintypes

EXTENSIONS = {
    "Fotos": [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".psd", ".ai", ".tif", ".tiff"],
    "Videos": [".mp4", ".mov", ".avi", ".wmv", ".mkv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".wma"],
    "PDF": [".pdf"],
    "Office": [".docx", ".xlsx", ".pptx", ".doc", ".xls", ".ppt"],
    "Archivos_de_texto": [".txt", ".csv"],
    "Programas": [".exe", ".msi", ".bat", ".sh"],
    "Imagen_ISO": [".iso"],
    "Archivos_para_comprimir": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

# Constantes para la función SHChangeNotify
SHCNE_ALLEVENTS = 0x7FFFFFFF
SHCNF_IDLIST = 0x0000
SHCNF_FLUSH = 0x1000

def get_extensions(path):
    extensions = set()
    for item in os.listdir(path):
        ext = os.path.splitext(item)[1]
        if ext != "":
            extensions.add(ext)
    return extensions

def create_dirs(path):
    extensions = get_extensions(path)
    for directory in EXTENSIONS.keys():
        if any(extension in EXTENSIONS[directory] for extension in extensions):
            directory_path = os.path.join(path, directory)
            if not os.path.exists(directory_path):
                os.mkdir(directory_path)

def move_files(path, file, ext):
    for directory, extensions in EXTENSIONS.items():
        if ext in extensions:
            try:
                shutil.move(os.path.join(path, file), os.path.join(path, directory))
            except Exception as e:
                print(f"Error al intentar mover el archivo {os.path.join(path, file)}. Error: {str(e)}")

def refresh_directory(path):
    # Notificar los cambios al shell
    ctypes.windll.shell32.SHChangeNotify(SHCNE_ALLEVENTS, SHCNF_IDLIST | SHCNF_FLUSH, None, None)

def organizer(path):
    create_dirs(path)
    for file in os.listdir(path):
        ext = os.path.splitext(file)[1]
        move_files(path, file, ext)
    
    refresh_directory(path)

while True:
    choice = input("Seleccione una opción:\n1. Ruta actual\n2. Introducir ruta personalizada\n")
    if choice == "1":
        current_directory = os.getcwd()
        organizer(current_directory)
        print(f"Proceso terminado. La ruta es {current_directory}")
    elif choice == "2":
        path = input("Ingrese la ruta que desea organizar: ")
        if os.path.exists(path):
            organizer(path)
            print(f"Proceso terminado. La ruta es {path}")
        else:
            print("Ruta no encontrada...")
    else:
        print("Opción no válida. Por favor, seleccione nuevamente.")

    refresh_choice = input("¿Desea organizar otra ruta? (s/n): ")
    if refresh_choice.lower() != "s":
        break