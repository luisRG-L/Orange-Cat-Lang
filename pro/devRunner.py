from OrangeCat import *

fileName = input("Project name: ")
code = getFileArray(PROJECTS + fileName + "\\main.ocat")
start_proccess(code)