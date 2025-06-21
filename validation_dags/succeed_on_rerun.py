from airflow.operators.python import PythonOperator
from airflow_config import DAG, load_config

from validation_dags.succeed_on_rerun_foo import _fail_on_first_run

config = load_config("config", "config")


with DAG(dag_id="lam-succeed-on-rerun-noconfig", config=config) as dag:
    fail_on_first = PythonOperator(task_id="lam-fail-on-first-run", python_callable=_fail_on_first_run)
