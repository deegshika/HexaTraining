from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_result_file():
    data = """Rahul,Pass
Priya,Fail
Amit,Pass
Sneha,Pass
Kiran,Fail
Megha,Pass"""
    with open("/tmp/results.txt", "w") as f:
        f.write(data)

def count_pass_fail():
    total_pass = 0
    total_fail = 0

    with open("/tmp/results.txt", "r") as f:
        for line in f:
            name, result = line.strip().split(",")
            if result == "Pass":
                total_pass += 1
            elif result == "Fail":
                total_fail += 1

    with open("/tmp/result_counts.txt", "w") as f:
        f.write(f"Total Pass = {total_pass}\n")
        f.write(f"Total Fail = {total_fail}\n")

def generate_result_summary():
    with open("/tmp/result_counts.txt", "r") as f:
        content = f.read()

    with open("/tmp/result_summary.txt", "w") as f:
        f.write("Exam Result Summary\n")
        f.write("===================\n")
        f.write(content)

with DAG(
    dag_id="exercise9_exam_result_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_result_file",
        python_callable=create_result_file
    )

    task2 = PythonOperator(
        task_id="count_pass_fail",
        python_callable=count_pass_fail
    )

    task3 = PythonOperator(
        task_id="generate_result_summary",
        python_callable=generate_result_summary
    )

    task1 >> task2 >> task3
