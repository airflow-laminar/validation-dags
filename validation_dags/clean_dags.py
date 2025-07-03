from airflow_config import Dag, load_config
from airflow_pydantic import DagCleanupTask

config = load_config("config", "config")

with Dag(dag_id="lam-clean-dags-noconfig", params=DagCleanupTask).instantiate(config=config) as dag:
    task = DagCleanupTask(task_id="lam-cleanup-dag-runs")
    task.instantiate(dag=dag)
