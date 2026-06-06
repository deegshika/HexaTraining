#Exercise 1
file=open("employees.txt","r")
print(file.read())
file.close()

#Exercise 2
file=open("employees.txt","r")
for line in file:
    print(line.strip())
file.close()

#Exercise 3
file=open("employees.txt","r")
count=0
for line in file:
    count+=1
print("Total Employees =",count)
file.close()

#Exercise 4
file=open("employees.txt","r")
for line in file:
    data=line.strip().split(",")
    print(data[1])
file.close()

#Exercise 5
file=open("employees.txt","r")
for line in file:
    data=line.strip().split(",")
    if data[4]=="Hyderabad":
        print(line.strip())
file.close()

#Exercise 6
file=open("employees.txt","r")
for line in file:
    data=line.strip().split(",")
    if data[4]=="Bangalore":
        print(line.strip())
file.close()

#Exercise 7
file=open("employees.txt","r")
for line in file:
    data=line.strip().split(",")
    if int(data[3])>80000:
        print(line.strip())
file.close()

#Exercise 8
file=open("employees.txt","r")
highest=0
for line in file:
    data=line.strip().split(",")
    salary=int(data[3])
    if salary>highest:
        highest=salary
print(highest)
file.close()

#Exercise 9
file=open("employees.txt","r")
lowest=999999
for line in file:
    data=line.strip().split(",")
    salary=int(data[3])
    if salary<lowest:
        lowest=salary
print(lowest)
file.close()

#Exercise 10
file=open("employees.txt","r")
total=0
count=0
for line in file:
    data=line.strip().split(",")
    total+=int(data[3])
    count+=1
print(total/count)
file.close()

# Exercise 11
file = open("employees.txt", "r")
total = 0
for line in file:
    data = line.strip().split(",")
    total += int(data[3])
print(total)
file.close()

# Exercise 12
file = open("employees.txt", "r")
count = 0
for line in file:
    data = line.strip().split(",")
    if data[2] == "AI Engineering":
        count += 1
print(count)
file.close()

# Exercise 13
file = open("employees.txt", "r")
count = 0
for line in file:
    data = line.strip().split(",")
    if data[2] == "Data Engineering":
        count += 1
print(count)
file.close()

# Exercise 14
file = open("employees.txt", "r")
for line in file:
    data = line.strip().split(",")
    if data[2] == "AI Engineering":
        print(line.strip())
file.close()

# Exercise 15
file = open("employees.txt", "r")
newfile = open("high_salary_employees.txt", "w")
for line in file:
    data = line.strip().split(",")
    if int(data[3]) > 80000:
        newfile.write(line)
file.close()
newfile.close()

# Exercise 16
file = open("employees.txt", "r")
newfile = open("hyderabad_employees.txt", "w")
for line in file:
    data = line.strip().split(",")
    if data[4] == "Hyderabad":
        newfile.write(line)
file.close()
newfile.close()

# Exercise 17
file = open("employees.txt", "r")
cities = set()
for line in file:
    data = line.strip().split(",")
    cities.add(data[4])
print(cities)
file.close()

# Exercise 18
file = open("employees.txt", "r")
data_engineering = 0
ai_engineering = 0
data_science = 0
cloud_engineering = 0

for line in file:
    data = line.strip().split(",")

    if data[2] == "Data Engineering":
        data_engineering += 1
    elif data[2] == "AI Engineering":
        ai_engineering += 1
    elif data[2] == "Data Science":
        data_science += 1
    elif data[2] == "Cloud Engineering":
        cloud_engineering += 1

print("Data Engineering =", data_engineering)
print("AI Engineering =", ai_engineering)
print("Data Science =", data_science)
print("Cloud Engineering =", cloud_engineering)

file.close()
