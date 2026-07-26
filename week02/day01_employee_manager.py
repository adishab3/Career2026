# import 
from week01.day06_functions_csv import (
count_employees_from_csv,
calculate_average_salary_from_csv,
find_highest_salary_from_csv)


print("=== Employee Manager ===")
print("1. Show all employees")
print("2. Show average salary")
print("3. Show highest salary")
print("4. Exit")

choice = input("Choose an option: ") #return str
print(choice)

#print(type(choice))

#if choice == "1":
 #   print("You chose option 1")

#if choice == "2":
 #   print("You chose option 2")

if choice == "1":
    count=count_employees_from_csv()
    print(f"There are {count} employees.")
elif choice == "2":
    avg=calculate_average_salary_from_csv()
    print(f"Average salary is: {int(avg)}")
elif choice == "3":
    employee = find_highest_salary_from_csv()
    print(f"Higest salary employee: {employee['name']} earns {employee['salary']}")
elif choice == "4":
    print("goodbye!")
else:
    print("Invalid option. Please try again.")

