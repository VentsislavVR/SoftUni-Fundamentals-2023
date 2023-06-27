company_employee_dict = {}

while True:
    data = input()
    if data == "End":
        break
    command = data.split(" -> ")
    company = command[0]
    employee_id = command[1]
    if company not in company_employee_dict:
        company_employee_dict[company] = []
    if employee_id not in company_employee_dict[company]:
        company_employee_dict[company].append(employee_id)

for com , emp in company_employee_dict.items():
    print(f"{com}")
    for e in emp:
        print(f"-- {e}")
