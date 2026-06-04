# Exercise 1
salaries=[45000,55000,65000,75000,85000]
print(salaries)

# Exercise 2
print(max(salaries))
print(min(salaries))

# Exercise 3
print(sum(salaries))

# Exercise 4
print(sum(salaries)/len(salaries))

# Exercise 5
salaries.append(95000)
salaries.append(105000)
print(salaries)

# Exercise 6
salaries.remove(55000)
print(salaries)

# Exercise 7
salaries.sort()
print(salaries)

# Exercise 8
salaries.sort(reverse=True)
print(salaries)

# Exercise 9
sorted_sal=sorted(salaries,reverse=True)
print(sorted_sal[1])

# Exercise 10
for sal in salaries:
    if sal>70000:
        print(sal)

# Exercise 11
employee=(101,"Rahul Sharma","Data Engineering",75000)
print(employee)

# Exercise 12
print(employee[1])

# Exercise 13
print(employee[2])

# Exercise 14
id,name,dept,salary=employee
print(id)
print(name)
print(dept)
print(salary)

# Exercise 15
print(len(employee))
print(employee[0])
print(employee[-1])

# Exercise 16
batch_a={"Rahul","Priya","Amit","Sneha","Farhan"}
batch_b={"Priya","Sneha","Neha","Arjun","Farhan"}
print(batch_a & batch_b)

# Exercise 17
print(batch_a - batch_b)

# Exercise 18
print(batch_b - batch_a)

# Exercise 19
print(batch_a | batch_b)

# Exercise 20
print(batch_a ^ batch_b)

# Exercise 21
employee_info={"employee_id":101,"name":"Rahul Sharma","department":"Data Engineering","salary":75000,"city":"Hyderabad"}
print(employee_info["name"])

# Exercise 22
print(employee_info["department"],employee_info["city"])

# Exercise 23
employee_info["experience"]=5
print(employee_info)

# Exercise 24
employee_info["salary"]=85000
print(employee_info)

# Exercise 25
del employee_info["city"]
print(employee_info)

# Exercise 26
print(list(employee_info.keys()))

# Exercise 27
print(list(employee_info.values()))

# Exercise 28
print(list(employee_info.items()))

# Exercise 29
employees=[
    {"id":101,"name":"Rahul","department":"IT","salary":50000},
    {"id":102,"name":"Priya","department":"HR","salary":70000},
    {"id":103,"name":"Amit","department":"IT","salary":60000},
    {"id":104,"name":"Sneha","department":"Finance","salary":80000},
    {"id":105,"name":"Farhan","department":"IT","salary":90000}
]
for emp in employees:
    print(emp["name"])

# Exercise 30
for emp in employees:
    if emp["department"]=="IT":
        print(emp)

# Exercise 31
highest=max(employees,key=lambda x:x["salary"])
print(highest)

# Exercise 32
lowest=min(employees,key=lambda x:x["salary"])
print(lowest)

# Exercise 33
total=sum(emp["salary"] for emp in employees)
print(total/len(employees))

# Exercise 34
print(total)

# Exercise 35
for emp in employees:
    if emp["salary"]>70000:
        print(emp)

# Exercise 36
it_count=sum(1 for emp in employees if emp["department"] == "IT")
print(it_count)

# Exercise 37
sorted_emps=sorted(employees,key=lambda x:x["salary"],reverse=True)
for emp in sorted_emps:
    print(emp["name"])

# Exercise 38
sorted_sal=sorted(employees,key=lambda x:x["salary"],reverse=True)
print(sorted_sal[1])

# Exercise 39
depts={emp["department"] for emp in employees}
print(depts)
