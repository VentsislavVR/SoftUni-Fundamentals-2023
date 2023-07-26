# import os
# path_to_root = os.path.dirname(os.path.abspath(__file__))
#
# file_path = os.path.join(path_to_root,"text.txt")
#
# if os.path.isfile(file_path):
#     print("File is here !")
# else:
#     print("File not found")

import os
path_to_root = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(path_to_root,"text.txt")
try:
    file =open(file_path,"r")
    content_lines = file.readline()
    print(content_lines,end="")
    # content_lines = file.read().split("\n")
    # print(content_lines)
    # while file.readline(): # for line in file: print(line,end="")
    #     print(file.readline())
    # print(file.read())
    # file.seek(25)
    # print(file.read())
    print("File is here !")
except FileNotFoundError:
    print("File not found")


