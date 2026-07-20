employees = [
    {"name": "Adi", "salary": 18000, "age": 31},
    {"name": "Dana", "salary": 25000, "age": 36},
    {"name": "Noa", "salary": 22000, "age": 29},
    {"name": "Shir", "salary": 15000, "age": 27}
]

# ערך באיבר

def employees_over_20k(employees):
    employees_over_20K=[]

    for employee in employees:
        if employee ['salary']>20000: 
            employees_over_20K.append(employee['name'])
    return employees_over_20K

result = employees_over_20k(employees)
print(result)

# איבר שלם

def employees_over_20k(employees):
    employees_over_20K=[]

    for employee in employees:
        if employee ['salary']>20000: 
            employees_over_20K.append(employee)
    return employees_over_20K

result = employees_over_20k(employees)
print(result)

# פונקציה שמחזירה לפי אותיות

def employee_names_start_with_a(employees):
    employees_start_a=[]

    for employee in employees:
        if employee['name'][0]=='A':
           employees_start_a.append(employee['name'])
    return employees_start_a 

result = employee_names_start_with_a(employees)
print(result)