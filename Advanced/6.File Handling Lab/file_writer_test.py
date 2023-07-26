import os
file_name="not"
path_to_root =os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root,file_name)

try:

    # file = open(file_path,"a")
    with open(file_path,"a") as file:
        file.write("\n2995")
        file.writelines(['\n'"K","Z"])
except FileNotFoundError:
    print("The fail is missing")