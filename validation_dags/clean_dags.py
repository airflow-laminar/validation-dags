from airflow_common_operators.tasks.dag_clean import DagCleanupParams, create_cleanup_dag_runs
from airflow_config import DAG, load_config

config = load_config("config", "config")

with DAG(
    dag_id="lam-clean-dags-noconfig",
    config=config,
    params=DagCleanupParams(),
) as dag:
    create_cleanup_dag_runs(
        task_id="lam-cleanup-dag-runs",
        dag=dag,
    )
