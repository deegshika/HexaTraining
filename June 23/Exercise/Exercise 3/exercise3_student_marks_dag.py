from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_marks_file():
    data = """Math,80
Science,75
English,90
Python,95"""
    
    with open("/tmp/marks.txt", "w") as f:
        f.write(data)

def calculate_average():
    total_marks = 0
    subject_count = 0

    with open("/tmp/marks.txt", "r") as f:
        for line in f:
            subject, marks = line.strip().split(",")
            total_marks += int(marks)
            subject_count += 1

    average = total_marks // subject_count if subject_count > 0 else 0

    with open("/tmp/marks_summary.txt", "w") as f:
        f.write(f"Average Marks = {average}\n")

def generate_result():
    with open("/tmp/marks_summary.txt", "r") as f:
        content = f.read()

    with open("/tmp/result.txt", "w") as f:
        f.write(content)
        if "Average Marks = 85" in content or int(content.strip().split("=")[1]) >= 40:
            f.write("Result = PASS\n")
        else:
            f.write("Result = FAIL\n")

with DAG(
    dag_id="exercise3_student_marks_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_marks_file",
        python_callable=create_marks_file
    )

    task2 = PythonOperator(
        task_id="calculate_average",
        python_callable=calculate_average
    )

    task3 = PythonOperator(
        task_id="generate_result",
        python_callable=generate_result
    )

    task1 >> task2 >> task3
