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
exec(open('./et_bizlogic_modular.py').read())

def_args ={
    "owner" : "airflow",
    "retries" : 0,
    "retry_delay" : timedelta(minutes =1),
    "start_date" : dtime(2024,12,13)
}

with DAG ("ALL_IN_ONE_Modular_etl",
         default_args = def_args,
         catchup =False) as dag:

    start = DummyOperator(task_id ="START")
    e_t_l = PythonOperator(task_id = "EXTRACT_TRANSFORM_LOAD", python_callable = etl, op_args = ["Learning DE", "ETL", "PIPELINES"], ) 
    end = DummyOperator(task_id ="END")


start >> e_t_l >> end 