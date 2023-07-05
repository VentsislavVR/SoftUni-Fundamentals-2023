employee_happiness = [int(el) for el in input().split()]

improvement_factor = int(input())
employee_happiness = [el * improvement_factor for el in employee_happiness]

avg_happiness = sum(employee_happiness) / len(employee_happiness)
happy_employees_count = len([el for el in employee_happiness if el >= avg_happiness])
half_employees_count = len(employee_happiness) / 2

if happy_employees_count >= half_employees_count:
    print(f"Score: {happy_employees_count}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_employees_count}/{len(employee_happiness)}. Employees are not happy!")
