from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_temperature_file():
    data = """Monday,34
Tuesday,36
Wednesday,31
Thursday,38
Friday,35
Saturday,33
Sunday,32"""
    
    with open("/tmp/temperature.txt", "w") as f:
        f.write(data)

def find_highest_temperature():
    highest_temp = 0
    highest_day = ""
    total_temp = 0
    count = 0

    with open("/tmp/temperature.txt", "r") as f:
        for line in f:
            day, temp = line.strip().split(",")
            temp = int(temp)

            total_temp += temp
            count += 1

            if temp > highest_temp:
                highest_temp = temp
                highest_day = day

    average_temp = total_temp / count if count > 0 else 0

    with open("/tmp/temperature_summary.txt", "w") as f:
        f.write(f"Highest Temperature = {highest_temp}\n")
        f.write(f"Highest Temperature Day = {highest_day}\n")
        f.write(f"Average Temperature = {round(average_temp, 2)}\n")

def generate_weather_report():
    with open("/tmp/temperature_summary.txt", "r") as f:
        content = f.read()

    with open("/tmp/weather_report.txt", "w") as f:
        f.write("Weather Report\n")
        f.write("==============\n")
        f.write(content)

with DAG(
    dag_id="exercise11_temperature_analysis_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_temperature_file",
        python_callable=create_temperature_file
    )

    task2 = PythonOperator(
        task_id="find_highest_temperature",
        python_callable=find_highest_temperature
    )

    task3 = PythonOperator(
        task_id="generate_weather_report",
        python_callable=generate_weather_report
    )

    task1 >> task2 >> task3
