from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_transactions():
    data = """Deposit,10000
Withdraw,2500
Deposit,4000
Withdraw,1500
Deposit,2000"""
    
    with open("/tmp/transactions.txt", "w") as f:
        f.write(data)

def calculate_balance():
    total_deposit = 0
    total_withdrawal = 0

    with open("/tmp/transactions.txt", "r") as f:
        for line in f:
            transaction_type, amount = line.strip().split(",")
            amount = int(amount)

            if transaction_type == "Deposit":
                total_deposit += amount
            elif transaction_type == "Withdraw":
                total_withdrawal += amount

    final_balance = total_deposit - total_withdrawal

    with open("/tmp/transaction_summary.txt", "w") as f:
        f.write(f"Total Deposit = {total_deposit}\n")
        f.write(f"Total Withdrawal = {total_withdrawal}\n")
        f.write(f"Final Balance = {final_balance}\n")

def generate_account_report():
    with open("/tmp/transaction_summary.txt", "r") as f:
        content = f.read()

    with open("/tmp/account_report.txt", "w") as f:
        f.write("Account Report\n")
        f.write("==============\n")
        f.write(content)

with DAG(
    dag_id="exercise12_bank_transaction_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_transactions",
        python_callable=create_transactions
    )

    task2 = PythonOperator(
        task_id="calculate_balance",
        python_callable=calculate_balance
    )

    task3 = PythonOperator(
        task_id="generate_account_report",
        python_callable=generate_account_report
    )

    task1 >> task2 >> task3
