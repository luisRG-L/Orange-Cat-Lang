import os
import shutil
from pathlib import Path

def getLineOf(code : str, number : int):
    return code[number]

def getFileArray(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            words = content.split()
            return words
    except:
        print("Error: Cannot open this source")
    
def getFile(file_path):
    archivo = Path('archivo.txt')
    contenido = archivo.read_text()
    print(contenido)

    
def createFile(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def createFolder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def deleteAll(folder):
    if not os.path.isdir(folder):
        raise ValueError(f"Error: '{folder}' don't exists.")

    for nombre in os.listdir(folder):
        complete_route = os.path.join(folder, nombre)
        if os.path.isfile(complete_route) or os.path.islink(complete_route):
            os.unlink(complete_route)
        elif os.path.isdir(complete_route):
            shutil.rmtree(complete_route)
