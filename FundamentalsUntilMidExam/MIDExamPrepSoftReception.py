first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_cunt = int(input())


answers_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

students_left = students_cunt - answers_per_hour
hours = 1
while students_left >= 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students_left -= answers_per_hour
    if students_left <= 0:
        print(f"Time needed: {hours}h.")
        break

