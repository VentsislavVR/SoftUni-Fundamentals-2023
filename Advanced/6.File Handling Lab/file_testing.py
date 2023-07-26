import os

absolute_path = os.path.dirname(os.path.abspath(__file__))  # current directory without hard coding it
# file_path = os.path.join(absolute_path, "testing", "testtest") # in testing
file_path = os.path.join(absolute_path,"text.txt") # in this folder
# file_dif_direct = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',"test_file")) # folder 5 error handling
print(file_path)

# try:
#     file = open(file_path, "r")
#     print(file.read())
# except FileNotFoundError:
#     print("No such file")
# else:
#     file.close()

# lines = file.readlines()

# for index in range(len(lines)):
#     cleared = ''.join(lines[index].split("\n"))
#     print(f"row {index+1} has {cleared}")
