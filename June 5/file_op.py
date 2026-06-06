file = open(
    "employees.txt",
    "r"
)
data =file.read()
print(data)
file.close()

file = open(
    "employees.txt","r"
)

print(file.readline())
file.close()

#multiple lines
lines = file.readlines()
print(lines)

# Automatically close the file object
with open(
    "employees.txt",
    "r"
) as file:
    data= file.read()
    print(data)

with open(
    "employees1.txt",
    "w"
) as file:
    file.write(
        "Rahul\n"
    )
    file.write(
        "Priya\n"
    )

# Append
with open(
    "employees1.txt",
    "a"
) as file:
    file.write(
        "Amit\n"
    )
