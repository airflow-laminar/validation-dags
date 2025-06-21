from airflow.operators.python import PythonOperator
from airflow_config import DAG, load_config

from validation_dags.dummy_foo import _dummy_foo

config = load_config("config", "config")


with DAG(dag_id="lam-dummy-noconfig", config=config) as dag:
    dummy_operator = PythonOperator(
        task_id="lam-dummy-task",
        python_callable=_dummy_foo,
    )
