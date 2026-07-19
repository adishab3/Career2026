def say_hello():
    print('Hello Adi')

say_hello()

def say_hello(name):
    print(f"Hello {name}")

say_hello("Adi")
say_hello("Dana")
say_hello("Noa")

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(10, 5)

print(result)

# תרגיל מסכם
employees = [
    {"name": "Adi", "salary": 18000, "age": 31},
    {"name": "Dana", "salary": 25000, "age": 36},
    {"name": "Noa", "salary": 22000, "age": 29},
    {"name": "Shir", "salary": 15000, "age": 27}
]

def calculate_avg_salary(employees):
    sum_salary=0
    for employee in employees:sum_salary +=employee["salary"]
    Avg_salary=sum_salary/len(employees)
    return Avg_salary

average= calculate_avg_salary(employees)
print (average)