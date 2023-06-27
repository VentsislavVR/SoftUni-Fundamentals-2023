line = input().split(" : ")

my_dict = {}
while len(line) != 1:
    course = line[0]
    student = line[1]
    if course not in my_dict:
        my_dict[course] = []
    my_dict[course].append(student)

    line = input().split(" : ")

for course, students in my_dict.items():
    print(f"{course}: {len(students)}")
    for s in students:
        print(f"-- {s}")
