try:
    a=10
    b=0

    result=a/b
    print(result)
except:
    print("Error occured")
print("Program Completed")


# specific exception
try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")

# another exception
try:
    age=int(input("Enter age:"))
    print(age)
except ValueError:
    print("Please enter a valid integer")


# multiple exception
try:
    age = int(input("Enter Age: "))
    print(100/age)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Age cannot be zero")

# Exception Object
try:
    num = int("abc")
except Exception as e:
    print(e)

#Else Block
try:
    num = 10
    print(num)
except:
    print("Error")
else:
    print("Success")

# Finally Block
try:
    print(10 / 0)
except:
    print("Error")
finally:
    print("Connection Closed")

#Raise Error
salary =-1000

if salary < 0:
    raise ValueError(
        "Salary cannot be negative"
)
