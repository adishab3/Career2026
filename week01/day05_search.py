
employees = [
    {"name": "Adi", "salary": 18000, "age": 31},
    {"name": "Dana", "salary": 25000, "age": 36},
    {"name": "Dana", "salary": 40000, "age": 40},
    {"name": "Noa", "salary": 22000, "age": 29},
    {"name": "Shir", "salary": 15000, "age": 27}
]


def find_employee_by_name(employees, name):
    employee_details= []

    for employee in employees:
            if employee['name'] == name: 
                   employee_details.append(employee)
                   
    if employee_details ==[] : return []
    else: return employee_details


employee = find_employee_by_name(employees, "Dana")
print(employee)

employee = find_employee_by_name(employees, "Moshe")
print(employee)
