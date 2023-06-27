def get_average_grade(grades):
    return sum(grades) / len(grades)


my_range = int(input())
winners = {}
for r in range(my_range):
    student = input()
    grade = float(input())

    if student not in winners:
        winners[student] = []
    winners[student].append(grade)

avrage_grade_by_student = {student: get_average_grade(grade) for student, grade in winners.items() if
                           get_average_grade(grade) >= 4.50}

# for student,grade in winners.items():
#     average_grade = sum(grade)/len(grade)
#     if average_grade < 4.50:
#         continue
#     print(f"{student} -> {average_grade:.2f}")
print(avrage_grade_by_student)
