import os

root_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "nott"
file_path = os.path.join(root_dir,file_name)

if os.path.isfile(file_name):
    os.remove(file_path)
else:
    print("File does not exist")


# try:
#     os.remove(file_path)
#     print("File does not exist(deleted)")
# except FileNotFoundError:
#     print("File not found")
