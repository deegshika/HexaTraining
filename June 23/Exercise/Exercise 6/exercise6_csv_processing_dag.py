from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import csv

def create_csv():
    data = """product,quantity,price
Laptop,2,70000
Mouse,5,500
Keyboard,3,1200"""
    
    with open("/tmp/sales.csv", "w") as f:
        f.write(data)

def read_csv():
    with open("/tmp/sales.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def calculate_revenue():
    revenues = []
    total_revenue = 0

    with open("/tmp/sales.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row["product"]
            quantity = int(row["quantity"])
            price = int(row["price"])
            revenue = quantity * price
            revenues.append((product, revenue))
            total_revenue += revenue

    with open("/tmp/revenue_summary.txt", "w") as f:
        for product, revenue in revenues:
            f.write(f"{product} = {revenue}\n")
        f.write(f"Total Revenue = {total_revenue}\n")

def create_summary():
    with open("/tmp/revenue_summary.txt", "r") as f:
        content = f.read()

    with open("/tmp/sales_report.txt", "w") as f:
        f.write("Sales Revenue Report\n")
        f.write("====================\n")
        f.write(content)

with DAG(
    dag_id="exercise6_csv_processing_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_csv",
        python_callable=create_csv
    )

    task2 = PythonOperator(
        task_id="read_csv",
        python_callable=read_csv
    )

    task3 = PythonOperator(
        task_id="calculate_revenue",
        python_callable=calculate_revenue
    )

    task4 = PythonOperator(
        task_id="create_summary",
        python_callable=create_summary
    )

    task1 >> task2 >> task3 >> task4
