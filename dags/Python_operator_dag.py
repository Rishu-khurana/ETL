from datetime import datetime as dtime
from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator


def extract():
    print("Logic to extract data")

def transform(a1):
    print("The value of ai is ", a1)
    print("Logic to transform data")

def load(p1,p2):
    print("the value of p1 is {}".format(p1))
    print("the value of p2 is {}".format(p2))

def_args ={
    "owner" : "airflow",
    "retries" : 0,
    "retry_delay" : timedelta(minutes =1),
    "start_date" : dtime(2024,12,13)
}

with DAG ("ex_python_operator",
         default_args = def_args,
         catchup =False) as dag:

    start = DummyOperator(task_id ="START")
    e = PythonOperator(
        task_id = "Extract",
        python_callable = extract
    )
    t = PythonOperator(
        task_id = "Transform",
        python_callable = transform,
        op_args = ["Learning ETL"]
    )
    
    l = PythonOperator(
        task_id = "Load",
        python_callable = load,
        op_args = ["ETL","AIRFLOW"]
    )
    end = DummyOperator(task_id ="END")


start >> e >> t >> l >> end