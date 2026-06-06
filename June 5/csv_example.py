import csv

with open('employees.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

    for row in reader:
        print(row[1])

#Count Employees
import csv
count=0
with open("employees.csv","r") as file:

    reader=csv.reader(file)
    next(reader)

    for row in reader:
        count+=1

print(count)

#Exercise 4
import csv

highest_salary=0

with open("employees.csv","r") as file:

    reader=csv.reader(file)

    next(reader)

    for row in reader:
        salary=int(row[3])

        if salary>highest_salary:
            highest_salary=salary

print(highest_salary)

#Exercise 5
import csv

lowest_salary=999999

with open("employees.csv","r") as file:

    reader=csv.reader(file)

    next(reader)

    for row in reader:
        salary=int(row[3])

        if salary<lowest_salary:
            lowest_salary=salary

print(lowest_salary)

#Exercise 6
import csv

total=0
count=0

with open("employees.csv","r") as file:

    reader=csv.reader(file)

    next(reader)

    for row in reader:
        total+=int(row[3])
        count+=1

print(total/count)

#Exercise 7
import csv

total=0

with open("employees.csv","r") as file:

    reader=csv.reader(file)

    next(reader)

    for row in reader:
        total+=int(row[3])

print(total)

#Exercise 8
import csv

with open("employees.csv","r") as file:

    reader=csv.reader(file)

    next(reader)

    for row in reader:
        if row[4]=="Hyderabad":
            print(row)

#Exercise 9
import csv

with open("employees.csv","r") as file:

    reader=csv.reader(file)

    next(reader)

    for row in reader:
        if row[2]=="AI Engineering":
            print(row)

#Exercise 10
import csv

with open("employees.csv","r") as file:

    reader=csv.reader(file)

    next(reader)

    for row in reader:
        if int(row[3])>80000:
            print(row)
