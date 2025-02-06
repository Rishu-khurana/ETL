from datetime import datetime as dtime
from datetime import timedelta
from airflow import DAG
#from airflow.hooks.postgres_hook import PostgresHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator

def get_iris_data():
    sql_stmnt = "SELECT * FROM iris"
    pg_hook = PostgresHook(
        postgres_conn_id = 'postgres_db',
        Database = 'postgres'
    )
    pg_conn = pg_hook.get_conn()
    cursor = pg_conn.cursor()
    cursor.execute(sql_stmnt)
    return cursor.fetchall()



with DAG(
    dag_id = 'postgres_db',
    schedule_interval = '@daily',
    start_date = dtime(year =2024, month=12, day=22),
    catchup =False
    
) as dag:
    task_get_iris_data = PythonOperator(
        task_id = 'get_iris_data',
        python_callable = get_iris_data,
        do_xcom_push = True
    )

       

