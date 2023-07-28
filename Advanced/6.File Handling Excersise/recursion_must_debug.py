import os


def save_extensions(dir_name):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(filename)
        elif os.path.isdir(file):
            save_extensions(file)


directory = input()

extensions = {}  # {.py:[__init__.py,example2.py],......}
result = []
save_extensions(directory)
# print(extensions)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension,files in extensions:
    result.append(f".{extension}")
    [result.append(f"---{file}")for file in sorted(files)]

with open("files/report.txt","w") as report_file:
    report_file.write('\n'.join(result))