from config import *;
from utilities import *;
from lexer import *;

file_name = input ("File route: ")
print("\n")
compressed_filename = input ("Compressed file name: ")
print ("\n\n")
code = getFileArray(PROJECTS + file_name + ".ocat")

tokenList = getTokenArray(code)

def transformToText():
    valueString = "%OCF\n%{\n\n"
    endString = "}%"
    for tokenValues in tokenList:
        valueString += " -", tokenValues[1], tokenValues[2] + "\n"
    valueString += endString
    return valueString

stringValue = transformToText()
createFile(PROJECTS + compressed_filename + ".ocf", stringValue)