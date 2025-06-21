from os import environ, path

from airflow.operators.bash import BashOperator
from airflow_config import DAG, load_config

config = load_config("config", "config")

with DAG(
    dag_id="lam-code-dags-noconfig",
    config=config,
):
    BashOperator(
        task_id="pull-dags-repo",
        bash_command="git fetch --all && git reset origin/main --hard",
        cwd=path.join(environ.get("AIRFLOW_HOME", "/var/lib/airflow"), "dag_src", "airflow-laminar", "validation-dags"),
        queue="primary",
    )
