from config import *
from basicCodes import *
from utilities import *

directory = input("Project name: ")
project_path = PROJECTS + directory
file_name = 'main.ocat'
complete = os.path.join(project_path, file_name)

libs_path = os.path.join(project_path, "\\libs")
libs_file_name = "libs.olib"
lib1_file_name = "lib1.ocat"
complete_olib = os.path.join(libs_path, libs_file_name)
complete_lib1 = os.path.join(libs_path, lib1_file_name)

createFolder(project_path)
createFile(complete, BASIC_CODE)

createFolder(libs_path)
createFile(complete_olib, OLIB_CODE)
createFile(complete_lib1, LIB_CODE)

print(f'Created dev project on: {complete}')