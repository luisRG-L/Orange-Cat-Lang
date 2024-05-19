import re

def getLineOf(code : str, number : int):
    return code[number]

def getFileArray(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        words = content.split()
        return words
