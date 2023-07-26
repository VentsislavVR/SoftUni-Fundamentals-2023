import os
file_name="nott"
path_to_root =os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root,file_name)

try:
    with open(file_path,"w") as file:
        file.write("first hand crafted file")
except FileNotFoundError:
    print("The fail is missing")
     