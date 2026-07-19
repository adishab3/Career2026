employees = [
    {"name": "Adi", "salary": 18000, "age": 31},
    {"name": "Dana", "salary": 25000, "age": 36},
    {"name": "Noa", "salary": 22000, "age": 29},
    {"name": "Shir", "salary": 15000, "age": 27}
]

def calculate_average_salary(employees):
    sum_salary=0
    for employee in employees:
        sum_salary +=employee["salary"]
    avg_salary=sum_salary/len(employees)
    return avg_salary

def count_employees_over_20k(employees):
    over_20K=0
    for employee in employees: 
        if employee['salary']>20000: over_20K+=1
    return over_20K

def find_highest_salary(employees):
    max_salary=0
    name=''
    
    for employee in employees:
        if employee['salary']>max_salary:
            max_salary=employee ["salary"]
            name=employee['name']
    return name,max_salary

average=calculate_average_salary(employees)
count=count_employees_over_20k(employees)
name,salary=find_highest_salary(employees)
print (average)
print(count)
print(name)
print(salary)
