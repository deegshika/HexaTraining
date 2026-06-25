from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_inventory():
    data = """Rice,50
Oil,7
Soap,35
Sugar,10
Tea,5"""
    
    with open("/tmp/inventory.txt", "w") as f:
        f.write(data)

def find_low_stock():
    low_stock_items = []

    with open("/tmp/inventory.txt", "r") as f:
        for line in f:
            product, stock = line.strip().split(",")
            stock = int(stock)

            if stock < 15:
                low_stock_items.append(product)

    with open("/tmp/low_stock.txt", "w") as f:
        for item in low_stock_items:
            f.write(item + "\n")

def generate_alert():
    with open("/tmp/low_stock.txt", "r") as f:
        content = f.read()

    with open("/tmp/alerts.txt", "w") as f:
        f.write(content)

with DAG(
    dag_id="exercise4_product_stock_alert_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_inventory",
        python_callable=create_inventory
    )

    task2 = PythonOperator(
        task_id="find_low_stock",
        python_callable=find_low_stock
    )

    task3 = PythonOperator(
        task_id="generate_alert",
        python_callable=generate_alert
    )

    task1 >> task2 >> task3
