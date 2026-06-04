# Tuple
cities=("Hyderabad","Mumbai","Delhi","Chennai","Pune")
print(cities)

# Indexing
print(cities[0])
print(cities[1])

# Negative Indexing
print(cities[-1])
print(cities[-2])

# Length
print(len(cities))

# Slicing
print(cities[1:4])

# Tuple is Immutable(Cannot Update)
# cities[1]="Bangalore"  Error

# Tuple Packing
employee=(101,"Rahul",75000)
print(employee)

# Tuple Unpacking
emp_id,emp_name,salary=employee

print(emp_id)
print(emp_name)
print(salary)

# Multiple Values Return
def get_employee():
    return 101,"Rahul",75000

result=get_employee()

print(result)

# Record as Tuple
record=(101,"Rahul","Hyderabad",75000)

print(record)

