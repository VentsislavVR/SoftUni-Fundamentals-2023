name_language_points = {}
banned = {}
while True:
    data = input()
    if data == "exam finished":
        break
    args = data.split("-")
    student_name = args[0]
    course_language = args[1]
    if course_language == "banned":
        banned[student_name] = name_language_points[student_name]
        continue
    points = int(args[2])
    if student_name not in name_language_points:
        name_language_points[student_name] = []
    name_language_points[student_name].append(course_language)
    name_language_points[student_name].append(points)
if student_name in banned.keys():
    wtf = name_language_points.pop(student_name)
print("Results:")
for stud, point in name_language_points.items():
    print(f"{stud} | {point[1]}")
if len(banned) > 0:
    name_language_points[student_name] = banned[student_name]
counting_dict = {}
for value in name_language_points.values():
    for lang in value:
        if lang not in counting_dict and not lang.isdigit():
            counting_dict[lang] = 1
        elif lang in counting_dict:
            counting_dict[lang] += 1
print("Submissions:")
for key, value in counting_dict.items():
    print(f"{key} - {value}")
