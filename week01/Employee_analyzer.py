employees = [
    {"name": "Adi", "salary": 18000, "age": 31},
    {"name": "Dana", "salary": 25000, "age": 36},
    {"name": "Noa", "salary": 22000, "age": 29},
    {"name": "Shir", "salary": 15000, "age": 27}
]

num_of_employees=len(employees)
print(f"Number of employees: {num_of_employees}")

sum_salary=0
for employee in employees:sum_salary +=employee["salary"]
Avg_salary=sum_salary/num_of_employees
print(f"Salary AVG of employees: {Avg_salary}")

Max_Salary=0
name=''
for employee in employees:
    if employee['salary']>Max_Salary:
     Max_Salary=employee ["salary"]
     Name=employee['name']
print(f"Max Salary: {Max_Salary},Name:{Name}")


Oldest_Employee=0
Name=''
for employee in employees:
    if employee['age']> Oldest_Employee :
        Oldest_Employee= employee ["age"]
        Name=employee['name']
print(f"Max age: {Oldest_Employee}"+f" Name:{Name}")

# Oldest_Employee=max(employees['age'])
# print(f"The Oldest employee: {Oldest_Employee}")

Over_20K=0
for employee in employees: 
    if employee['salary']>20000: Over_20K+=1

print(f"The amount of employees over 20K: {Over_20K}")


