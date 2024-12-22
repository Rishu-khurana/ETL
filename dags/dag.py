from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Corrected start_date as a datetime object
def_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 12, 8)  # Corrected this line
}

with DAG("ETL",
         catchup=False,
         default_args=def_args) as dag:
    start = DummyOperator(task_id="start")
    e = DummyOperator(task_id="extract")
    t = DummyOperator(task_id="transform")
    l = DummyOperator(task_id="load")
    endd = DummyOperator(task_id="END")

    # Define task dependencies
    start >> e >> t >> l >> endd
