from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_bill_file():
    data = """Rahul,210
Priya,180
Amit,300
Sneha,150
Kiran,260"""
    with open("/tmp/electricity.txt", "w") as f:
        f.write(data)

def calculate_total_units():
    total_units = 0
    customer_count = 0

    with open("/tmp/electricity.txt", "r") as f:
        for line in f:
            name, units = line.strip().split(",")
            total_units += int(units)
            customer_count += 1

    average_units = total_units / customer_count if customer_count > 0 else 0

    with open("/tmp/electricity_totals.txt", "w") as f:
        f.write(f"Customers = {customer_count}\n")
        f.write(f"Total Units = {total_units}\n")
        f.write(f"Average Units = {int(average_units)}\n")

def generate_bill_summary():
    with open("/tmp/electricity_totals.txt", "r") as f:
        content = f.read()

    with open("/tmp/bill_summary.txt", "w") as f:
        f.write(content)

with DAG(
    dag_id="exercise8_electricity_bill_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_bill_file",
        python_callable=create_bill_file
    )

    task2 = PythonOperator(
        task_id="calculate_total_units",
        python_callable=calculate_total_units
    )

    task3 = PythonOperator(
        task_id="generate_bill_summary",
        python_callable=generate_bill_summary
    )

    task1 >> task2 >> task3
