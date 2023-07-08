import os
import shutil

while True:
    path = input("Dame la ruta la cual quieres organizar: ")
    if os.path.exists(path):
        path+="/"
        break
    
    print("Ruta no encontrada...")



print(f"proceso terminado. la ruta es {path} ")
    
    