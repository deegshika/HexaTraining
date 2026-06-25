from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_orders():
    data = """product,quantity,price
Laptop,1,70000
Mouse,4,500
Monitor,2,12000
Keyboard,3,1500"""
    
    with open("/tmp/orders.csv", "w") as f:
        f.write(data)

def calculate_order_value():
    total_revenue = 0
    highest_product = ""
    highest_revenue = 0

    with open("/tmp/orders.csv", "r") as f:
        lines = f.readlines()[1:]  # skip header

        for line in lines:
            product, quantity, price = line.strip().split(",")
            revenue = int(quantity) * int(price)
            total_revenue += revenue

            if revenue > highest_revenue:
                highest_revenue = revenue
                highest_product = product

    with open("/tmp/order_summary.txt", "w") as f:
        f.write(f"Total Revenue = {total_revenue}\n")
        f.write(f"Highest Selling Product = {highest_product}\n")

def generate_sales_report():
    with open("/tmp/order_summary.txt", "r") as f:
        content = f.read()

    with open("/tmp/sales_report.txt", "w") as f:
        f.write("Sales Report\n")
        f.write("============\n")
        f.write(content)

with DAG(
    dag_id="exercise10_online_orders_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_orders",
        python_callable=create_orders
    )

    task2 = PythonOperator(
        task_id="calculate_order_value",
        python_callable=calculate_order_value
    )

    task3 = PythonOperator(
        task_id="generate_sales_report",
        python_callable=generate_sales_report
    )

    task1 >> task2 >> task3
