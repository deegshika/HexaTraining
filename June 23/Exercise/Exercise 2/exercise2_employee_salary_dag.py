from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_salary_file():
    data = """Rahul,45000
Priya,52000
Amit,61000
Sneha,48000"""
    
    with open("/tmp/employees.txt", "w") as f:
        f.write(data)

def calculate_total_salary():
    total_salary = 0
    employee_count = 0

    with open("/tmp/employees.txt", "r") as f:
        for line in f:
            name, salary = line.strip().split(",")
            total_salary += int(salary)
            employee_count += 1

    with open("/tmp/salary_summary.txt", "w") as f:
        f.write(f"Employees = {employee_count}\n")
        f.write(f"Total Salary = {total_salary}\n")

def generate_report():
    with open("/tmp/salary_summary.txt", "r") as f:
        content = f.read()

    with open("/tmp/report.txt", "w") as f:
        f.write("Salary Report\n")
        f.write(content)

with DAG(
    dag_id="exercise2_employee_salary_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_salary_file",
        python_callable=create_salary_file
    )

    task2 = PythonOperator(
        task_id="calculate_total_salary",
        python_callable=calculate_total_salary
    )

    task3 = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report
    )

    task1 >> task2 >> task3
