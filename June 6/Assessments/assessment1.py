#Task 1
import csv

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#Task 2
import csv

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        print(row)

#Task 3
import csv

count=0

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        count+=1

print(count)

#Task 4
import csv

total_revenue=0

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        revenue=int(row[5])*int(row[6])
        total_revenue+=revenue

print(total_revenue)

#Task 5
import csv

highest_order=0

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        order_value=int(row[5])*int(row[6])

        if order_value>highest_order:
            highest_order=order_value

print(highest_order)

#Task 6
import csv

lowest_order=99999999

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        order_value=int(row[5])*int(row[6])

        if order_value<lowest_order:
            lowest_order=order_value

print(lowest_order)

#Task 7
import csv

total=0
count=0

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        order_value=int(row[5])*int(row[6])
        total+=order_value
        count+=1

print(total/count)

#Task 8
import csv

customers=set()

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        customers.add(row[1])

print(customers)

#Task 9
import csv

customers=set()

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        customers.add(row[1])

print(len(customers))

#Task 10
import csv

highest_purchase=0
top_customer=""

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        purchase=int(row[5])*int(row[6])

        if purchase>highest_purchase:
            highest_purchase=purchase
            top_customer=row[1]

print(top_customer,highest_purchase)

#Task 11
import csv

product_count={}

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        product=row[3]

        if product in product_count:
            product_count[product]+=1
        else:
            product_count[product]=1

print(product_count)

#Task 12
import csv

product_revenue={}

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        product=row[3]
        revenue=int(row[5])*int(row[6])

        if product in product_revenue:
            product_revenue[product]+=revenue
        else:
            product_revenue[product]=revenue

print(product_revenue)

#Task 13
import csv

product_quantity={}

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        product=row[3]
        quantity=int(row[5])

        if product in product_quantity:
            product_quantity[product]+=quantity
        else:
            product_quantity[product]=quantity

top_product=max(product_quantity,key=product_quantity.get)

print(top_product)

#Task 14
import csv

product_quantity={}

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        product=row[3]
        quantity=int(row[5])

        if product in product_quantity:
            product_quantity[product]+=quantity
        else:
            product_quantity[product]=quantity

least_product=min(product_quantity,key=product_quantity.get)

print(least_product)

#Task 15
import csv

category_revenue={}

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        category=row[4]
        revenue=int(row[5])*int(row[6])

        if category in category_revenue:
            category_revenue[category]+=revenue
        else:
            category_revenue[category]=revenue

print(category_revenue)

#Task 16
import csv

city_count={}

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        city=row[2]

        if city in city_count:
            city_count[city]+=1
        else:
            city_count[city]=1

print(city_count)

#Task 17
import csv

city_revenue={}

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        city=row[2]
        revenue=int(row[5])*int(row[6])

        if city in city_revenue:
            city_revenue[city]+=revenue
        else:
            city_revenue[city]=revenue

print(city_revenue)

#Task 18
import csv

city_revenue={}

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        city=row[2]
        revenue=int(row[5])*int(row[6])

        if city in city_revenue:
            city_revenue[city]+=revenue
        else:
            city_revenue[city]=revenue

top_city=max(city_revenue,key=city_revenue.get)

print(top_city)

#Task 19
import csv

products=[]

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        products.append(row[3])

products.sort()

print(products)

#Task 20
import csv

cities=set()

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        cities.add(row[2])

print(cities)

#Task 21
import csv

city_revenue={}

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        city=row[2]
        revenue=int(row[5])*int(row[6])

        if city in city_revenue:
            city_revenue[city]+=revenue
        else:
            city_revenue[city]=revenue

print(city_revenue)

#Task 22
import csv

product_quantity={}

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        product=row[3]
        quantity=int(row[5])

        if product in product_quantity:
            product_quantity[product]+=quantity
        else:
            product_quantity[product]=quantity

print(product_quantity)

#Task 23
def calculate_total_revenue():

    import csv

    total_revenue=0

    with open("orders.csv","r") as file:
        reader=csv.reader(file)
        next(reader)

        for row in reader:
            revenue=int(row[5])*int(row[6])
            total_revenue+=revenue

    print(total_revenue)

calculate_total_revenue()

#Task 24
def find_top_product():

    import csv

    product_quantity={}

    with open("orders.csv","r") as file:
        reader=csv.reader(file)
        next(reader)

        for row in reader:
            product=row[3]
            quantity=int(row[5])

            if product in product_quantity:
                product_quantity[product]+=quantity
            else:
                product_quantity[product]=quantity

    top_product=max(product_quantity,key=product_quantity.get)

    print(top_product)

find_top_product()

#Task 25
def find_top_city():

    import csv

    city_revenue={}

    with open("orders.csv","r") as file:
        reader=csv.reader(file)
        next(reader)

        for row in reader:
            city=row[2]
            revenue=int(row[5])*int(row[6])

            if city in city_revenue:
                city_revenue[city]+=revenue
            else:
                city_revenue[city]=revenue

    top_city=max(city_revenue,key=city_revenue.get)

    print(top_city)

find_top_city()

#Task 26
def find_average_order_value():

    import csv

    total=0
    count=0

    with open("orders.csv","r") as file:
        reader=csv.reader(file)
        next(reader)

        for row in reader:
            order_value=int(row[5])*int(row[6])
            total+=order_value
            count+=1

    print(total/count)

find_average_order_value()

#Task 27
try:

    import csv

    with open("orders.csv","r") as file:
        reader=csv.reader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("File not found")

#Task 28
import csv

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:

        try:
            quantity=int(row[5])
            print(quantity)

        except ValueError:
            print("Invalid quantity value")

#Task 29
import csv

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:

        try:
            price=int(row[6])
            print(price)

        except ValueError:
            print("Invalid price value")

#Task 30
import numpy as np
import csv

order_values=[]

with open("orders.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        revenue=int(row[5])*int(row[6])
        order_values.append(revenue)

arr=np.array(order_values)

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))

#Task 31
import pandas as pd

df=pd.read_csv("orders.csv")

print(df)

#Task 32
import pandas as pd

df=pd.read_csv("orders.csv")

df["Revenue"]=df["quantity"]*df["price"]

print(df)

#Task 33
import pandas as pd

df=pd.read_csv("orders.csv")

df["Revenue"]=df["quantity"]*df["price"]

print(df.sort_values(by="Revenue",ascending=False).head(5))

#Task 34
import pandas as pd

df=pd.read_csv("orders.csv")

df["Revenue"]=df["quantity"]*df["price"]

print(df.groupby("city")["Revenue"].sum())

#Task 35
import pandas as pd

df=pd.read_csv("orders.csv")

df["Revenue"]=df["quantity"]*df["price"]

print(df.groupby("product")["Revenue"].sum())

#Task 36
import pandas as pd

df=pd.read_csv("orders.csv")

print(df["product"].value_counts())

#Task 37
import pandas as pd

df=pd.read_csv("orders.csv")

print(df["city"].value_counts())

#Task 38
import pandas as pd

df=pd.read_csv("orders.csv")

df["Revenue"]=df["quantity"]*df["price"]

high_value=df[df["Revenue"]>50000]

high_value.to_csv("high_value_orders.csv",index=False)

print("File created")

#Task 39
import pandas as pd

df=pd.read_csv("orders.csv")

electronics=df[df["category"]=="Electronics"]

electronics.to_csv("electronics_orders.csv",index=False)

print("File created")

#Task 40
while True:

    print("1.View Orders")
    print("2.Revenue Analysis")
    print("3.Product Analysis")
    print("4.City Analysis")
    print("5.Export Reports")
    print("6.Exit")

    choice=int(input("Enter choice:"))

    if choice==1:
        print("Viewing Orders")

    elif choice==2:
        print("Revenue Analysis")

    elif choice==3:
        print("Product Analysis")

    elif choice==4:
        print("City Analysis")

    elif choice==5:
        print("Export Reports")

    elif choice==6:
        print("Exited")
        break

    else:
        print("Invalid choice")
