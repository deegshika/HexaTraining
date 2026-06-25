from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_employee_file():
    data = """Rahul,28
Priya,31
Amit,42
Sneha,26
Kiran,38"""
    
    with open("/tmp/employees.txt", "w") as f:
        f.write(data)

def calculate_average_age():
    youngest_name = ""
    youngest_age = 999
    oldest_name = ""
    oldest_age = 0
    total_age = 0
    count = 0

    with open("/tmp/employees.txt", "r") as f:
        for line in f:
            name, age = line.strip().split(",")
            age = int(age)

            total_age += age
            count += 1

            if age < youngest_age:
                youngest_age = age
                youngest_name = name

            if age > oldest_age:
                oldest_age = age
                oldest_name = name

    average_age = total_age / count if count > 0 else 0

    with open("/tmp/employee_age_summary.txt", "w") as f:
        f.write(f"Youngest Employee = {youngest_name} ({youngest_age})\n")
        f.write(f"Oldest Employee = {oldest_name} ({oldest_age})\n")
        f.write(f"Average Age = {round(average_age, 2)}\n")

def generate_age_report():
    with open("/tmp/employee_age_summary.txt", "r") as f:
        content = f.read()

    with open("/tmp/age_report.txt", "w") as f:
        f.write("Employee Age Report\n")
        f.write("===================\n")
        f.write(content)

with DAG(
    dag_id="exercise13_employee_age_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_employee_file",
        python_callable=create_employee_file
    )

    task2 = PythonOperator(
        task_id="calculate_average_age",
        python_callable=calculate_average_age
    )

    task3 = PythonOperator(
        task_id="generate_age_report",
        python_callable=generate_age_report
    )

    task1 >> task2 >> task3
