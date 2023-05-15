# BONUS SCORING SYSTEM
#
# •	On the first line, you are going to receive the number of the students – an integer in the range [0…50]
# •	On the second line, you will receive the number of the lectures – an integer number in the range [0...50].
# •	On the third line, you will receive the additional bonus – an integer number in the range [0….100].
# •	On the following lines, you will be receiving the attendance of each student.


# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
# Find the student with the maximum bonus and print them, along with his attendance, in the following format:
# "Max Bonus: {max bonus points}."
# "The student has attended {student attendances} lectures."
from math import ceil
students = int(input())
lectures = int(input())
bonus = int(input())

max_attendances = 0

for i in range(students):
    attendances = int(input())
    max_attendances = max(attendances,max_attendances)
total_bonus = 0
if lectures !=0:
    total_bonus = (max_attendances/lectures) * (5 + bonus)

print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")
