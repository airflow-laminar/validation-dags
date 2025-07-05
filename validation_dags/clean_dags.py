from airflow_config import Dag, load_config
from airflow_pydantic import DagClean, DagCleanTaskArgs

config = load_config("config", "config")

with Dag(dag_id="lam-clean-dags-noconfig", params=DagCleanTaskArgs).instantiate(config=config) as dag:
    task = DagClean(task_id="lam-cleanup-dag-runs", dag=dag)
