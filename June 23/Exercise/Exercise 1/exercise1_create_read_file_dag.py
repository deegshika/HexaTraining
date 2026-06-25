from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_file():
    content = """Welcome to Apache Airflow
Learning DAGs
Learning Task Dependencies"""

    with open("/tmp/message.txt", "w") as f:
        f.write(content)

def read_file():
    with open("/tmp/message.txt", "r") as f:
        print(f.read())

with DAG(
    dag_id="exercise1_create_read_file_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_file",
        python_callable=create_file
    )

    task2 = PythonOperator(
        task_id="read_file",
        python_callable=read_file
    )

    task1 >> task2
