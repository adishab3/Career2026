# first demonstration of file reading

#import csv 
#with open("week01/employees.csv") as file:
   # print (file.read())


# The right way to read from a file 
# save All as txt ~ str
import csv

with open("week01/employees.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        #no filter
        print(row) 

        # by name,salary,age
        #print(row['name']),print(row['salary']),print(row['age'])

        # by city
        # print (row['city']) ~ KeyError - no colomn city in dict

        # new santance 
        #print (row['name']+f" earns "+row['salary'])
        #print (f"{row['name']} earns {row['salary']}")
    
        #employees over 20K
        #if int(row['salary']) >20000 :
            #print(row)

    



