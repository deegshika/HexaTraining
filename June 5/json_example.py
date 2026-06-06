import json

employees = [

    {
        "employee_id": 101,
        "name": "Rahul Sharma",
        "department": "Data Engineering",
        "salary": 75000,
        "city": "Hyderabad"
    },

    {
        "employee_id": 102,
        "name": "Priya Reddy",
        "department": "AI Engineering",
        "salary": 85000,
        "city": "Bangalore"
    },

    {
        "employee_id": 103,
        "name": "Amit Kumar",
        "department": "Data Engineering",
        "salary": 65000,
        "city": "Mumbai"
    },

    {
        "employee_id": 104,
        "name": "Sneha Patel",
        "department": "Data Science",
        "salary": 95000,
        "city": "Chennai"
    },

    {
        "employee_id": 105,
        "name": "Farhan Ali",
        "department": "Cloud Engineering",
        "salary": 80000,
        "city": "Delhi"
    }

]

with open('employees.json', 'w') as file:
    json.dump(employees, file,indent=4)

print("JSON file created successfully")

# Find Employee With Highest Salary
highest_salary=0
highest_employee=""

for employee in employees:
    if employee["salary"]>highest_salary:
        highest_salary=employee["salary"]
        highest_employee=employee["name"]

print(highest_employee,highest_salary)

# Find Average Salary
total=0

for employee in employees:
    total+=employee["salary"]

average=total/len(employees)
print(average)

# Display Data Engineering Employees
for employee in employees:
    if employee["department"]=="Data Engineering":
        print(employee)

# Display Employees Earning More Than 80000
for employee in employees:
    if employee["salary"]>80000:
        print(employee)

# Update Salary of One Employee
for employee in employees:
    if employee["employee_id"]==101:
        employee["salary"]=78000

print(employees)

# Add New Employee
new_employee={
    "employee_id":106,
    "name":"Neha Singh",
    "department":"AI Engineering",
    "salary":72000,
    "city":"Hyderabad"
}

employees.append(new_employee)
print(employees)

# Delete an Employee
for employee in employees:
    if employee["employee_id"]==103:
        employees.remove(employee)

print(employees)
