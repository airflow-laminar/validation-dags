from airflow_common_operators.tasks.dag_clean import DagCleanupTask
from airflow_config import Dag, load_config

config = load_config("config", "config")

with Dag(
    dag_id="lam-clean-dags-noconfig",
    params=DagCleanupTask,
).instantiate(config=config) as dag:
    task = DagCleanupTask(task_id="lam-cleanup-dag-runs")
    task.instantiate(dag=dag)
