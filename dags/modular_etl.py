from datetime import datetime as dtime
from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator

import pandas as pd
import os

root_folder = "/Users/rishukhurana/airflow/pyscripts"
os.chdir(root_folder)

exec(open('./init.py').read())
exec(open('./etl_bizlogic.py').read())

def_args ={
    "owner" : "airflow",
    "retries" : 0,
    "retry_delay" : timedelta(minutes =1),
    "start_date" : dtime(2024,12,13)
}

with DAG ("Modular_etl",
         default_args = def_args,
         catchup =False) as dag:

    start = DummyOperator(task_id ="START")
    e = PythonOperator(
        task_id = "Extract",
        python_callable = extract,
        do_xcom_push =True

    )
    t = PythonOperator(
        task_id = "Transform",
        python_callable = transform,
        op_args = ["Learning ETL"],
        do_xcom_push =True
    )
    
    l = PythonOperator(
        task_id = "Load",
        python_callable = load,
        op_args = ["ETL","AIRFLOW"],
        do_xcom_push =True
    )
    end = DummyOperator(task_id ="END")


start >> e >> t >> l >> end 