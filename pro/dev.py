from config import *
import os
from basicCodes import *

directory = input("Project name: ")
file_path = PROJECTS + directory
file_name = 'main.ocat'
complete = os.path.join(file_path, file_name)

if not os.path.exists(file_path):
    os.makedirs(file_path)
else:
    print("This project already exists")
    
with open(complete, 'w') as file:
    file.write(BASIC_CODE)

print(f'Created dev project on: {complete}')