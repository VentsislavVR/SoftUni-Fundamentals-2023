first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_cunt = int(input())


answers_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

hours = 0
total_time = 0
while students_cunt > 0:
    hours += 1
    total_time += 1
    if hours % 4 == 0:
        continue
    students_cunt -= answers_per_hour

print(f"Time needed: {hours}h.")


