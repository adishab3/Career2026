
import csv

# Calculate the average salary of all employees from CSV file
def calculate_average_salary_from_csv():
    sum_salary = 0
    count = 0

    with open("week01/employees.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
            sum_salary += int(row['salary'])
            count += 1

    return sum_salary / count

avg=calculate_average_salary_from_csv()
#print(avg)


# # Return a list of employees with salary above the given threshold from CSV file
def employees_over_salary_from_csv(employees_salary):
    employees_over=[]

    with open("week01/employees.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if int(row['salary'])> employees_salary:
                 employees_over.append(row)
        return employees_over
        
result = employees_over_salary_from_csv(20000)

#print(result)

# # Find the employee with the highest salary from CSV file
def find_highest_salary_from_csv():
    highest_salary=0
    #employees_highest_salary=row

    with open("week01/employees.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if int(row['salary'])> highest_salary:
                 highest_salary=int(row['salary'])
                 employees_highest_salary=row

        return employees_highest_salary
        
result = find_highest_salary_from_csv()
print(result)

# Count the number of employees in the CSV file
def count_employees_from_csv():
    count=0

    with open("week01/employees.csv") as file:
        reader=csv.DictReader(file)

        for row in reader:
            count += 1 
        return count

        
result = count_employees_from_csv()
print(result)


# Find all employees older than the given age from CSV file
def employees_over_age_from_csv(age):
    employees_over_age_from_csv=[]
        
    with open("week01/employees.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if int(row['age'])> age:
                 employees_over_age_from_csv.append(row)

        return employees_over_age_from_csv

result = employees_over_age_from_csv(30)
print(result)

# Find all employee names that start with the given letter
def employees_name_starts_with_from_csv(letter):
    employees_name_starts_with=[]
        
    with open("week01/employees.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name=row["name"]
            if name[0] == letter:
                 employees_name_starts_with.append(row["name"])

        return employees_name_starts_with

result = employees_name_starts_with_from_csv("D")
print(result)