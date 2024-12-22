from datetime import datetime as dtime
from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator

import pandas as pd

Name = "Rishu"

def extract():
    print("What is your name")
    print("My name is", Name)
    rtn_val = "I got this!"
    return rtn_val

def transform(a1):
    xcom_pull_obj = ti.xcom_pull(task_ids = ["Extract"])
    print("type of xcom object is {}".format(type(xcom_pull_obj)))
    extract_rtn_obj = xcom_pull_obj[0]
    print("the value of xcom pull back obj is {extract_rtn_obj}")
    print("The value of ai is ", a1)
    print("Logic to transform data")
    return 10

def load(p1,p2,ti):
    xcom_pull_obj = ti.xcom_pull(task_ids = ["Extract"])
    print("type of xcom object is {}".format(type(xcom_pull_obj)))
    print("the value of xcom pull back obj is {}".format(xcom_pull_obj[0]))
    print("the value of p1 is {}".format(p1))
    print("the value of p2 is {}".format(p2))

def_args ={
    "owner" : "airflow",
    "retries" : 0,
    "retry_delay" : timedelta(minutes =1),
    "start_date" : dtime(2024,12,13)
}

with DAG ("X_coms",
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