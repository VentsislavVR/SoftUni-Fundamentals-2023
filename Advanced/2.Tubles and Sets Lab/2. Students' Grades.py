from statistics import mean
from collections import defaultdict

num = int(input())
students = defaultdict(lambda: [])

for stud in range(num):
    student, grade = input().split()
    grade = float(grade)
    students[student].append(grade)

for name, grades in students.items():
    # avg = mean(grades)
    avg = sum(grades) / len(grades)

    print(f"{name} -> {' '.join(str(f'{grade:.2f}') for grade in grades)} (avg: {avg:.2f})")




# from statistics import mean
# from collections import defaultdict
# num = int(input())
# students = {}
#
#
# for stud in range(num):
#     student,grade = input().split()
#     grade = float(grade)
#     if student not in students:
#         students[student] = []
#     students[student].append(grade)
#
#
# for name ,grades in students.items():
#     avg = mean(grades)
#
#     print(f"{name} -> {' '.join(str(f'{grade:.2f}') for grade in grades)} (avg: {avg:.2f})")

# from collections import defaultdict
#
# student_count = defaultdict(lambda:0)
# student_count["a"] += 1
# print(student_count)