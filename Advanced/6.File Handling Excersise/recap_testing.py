import os
from datetime import datetime
file_path = "files/example.txt" # "../files/example.txt" # ../ one directory back

with open(file_path,"w") as file:
    file.write("working with files is cool\n")

with open(file_path,"r") as file:
    print(file.read())
    file.seek(0)
    print(file.readlines())
file_info = os.stat(file_path)
print(f"file size {file_info.st_size} bytes")
print(f"Last modified: {datetime.fromtimestamp(int(file_info.st_mtime))}")

os.rename(file_path,"files/new_name.txt")