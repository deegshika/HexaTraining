from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_attendance():
    data = """Rahul,Present
Priya,Present
Amit,Absent
Sneha,Present
Kiran,Absent"""
    
    with open("/tmp/attendance.txt", "w") as f:
        f.write(data)

def count_present():
    present_count = 0
    total_students = 0

    with open("/tmp/attendance.txt", "r") as f:
        for line in f:
            name, status = line.strip().split(",")
            total_students += 1
            if status == "Present":
                present_count += 1

    with open("/tmp/present_summary.txt", "w") as f:
        f.write(f"Total Students = {total_students}\n")
        f.write(f"Present = {present_count}\n")

def count_absent():
    absent_count = 0

    with open("/tmp/attendance.txt", "r") as f:
        for line in f:
            name, status = line.strip().split(",")
            if status == "Absent":
                absent_count += 1

    with open("/tmp/absent_summary.txt", "w") as f:
        f.write(f"Absent = {absent_count}\n")

def generate_summary():
    with open("/tmp/present_summary.txt", "r") as f:
        present_data = f.read()

    with open("/tmp/absent_summary.txt", "r") as f:
        absent_data = f.read()

    with open("/tmp/attendance_report.txt", "w") as f:
        f.write("Attendance Report\n")
        f.write("=================\n")
        f.write(present_data)
        f.write(absent_data)

with DAG(
    dag_id="exercise5_attendance_report_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_attendance",
        python_callable=create_attendance
    )

    task2 = PythonOperator(
        task_id="count_present",
        python_callable=count_present
    )

    task3 = PythonOperator(
        task_id="count_absent",
        python_callable=count_absent
    )

    task4 = PythonOperator(
        task_id="generate_summary",
        python_callable=generate_summary
    )

    task1 >> task2 >> task3 >> task4
