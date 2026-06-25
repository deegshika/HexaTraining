from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_enrollment_file():
    data = """Python,Rahul
Python,Priya
SQL,Amit
Python,Sneha
Power BI,Kiran
SQL,Megha
Power BI,Arjun"""
    
    with open("/tmp/enrollments.txt", "w") as f:
        f.write(data)

def count_students():
    course_counts = {}

    with open("/tmp/enrollments.txt", "r") as f:
        for line in f:
            course, student = line.strip().split(",")
            course_counts[course] = course_counts.get(course, 0) + 1

    with open("/tmp/course_counts.txt", "w") as f:
        for course, count in course_counts.items():
            f.write(f"{course} = {count}\n")

def generate_course_report():
    with open("/tmp/course_counts.txt", "r") as f:
        content = f.read()

    with open("/tmp/course_report.txt", "w") as f:
        f.write("Course Enrollment Report\n")
        f.write("========================\n")
        f.write(content)

with DAG(
    dag_id="exercise14_course_enrollment_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_enrollment_file",
        python_callable=create_enrollment_file
    )

    task2 = PythonOperator(
        task_id="count_students",
        python_callable=count_students
    )

    task3 = PythonOperator(
        task_id="generate_course_report",
        python_callable=generate_course_report
    )

    task1 >> task2 >> task3
