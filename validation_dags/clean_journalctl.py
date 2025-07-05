from airflow_common_operators import JournalctlClean, JournalctlCleanTaskArgs
from airflow_config import Dag, load_config

config = load_config("config", "config")

with Dag(dag_id="lam-clean-journalctl-noconfig", params=JournalctlCleanTaskArgs).instantiate(config=config) as dag:
    task = JournalctlClean(task_id="lam-cleanup-journalctl", dag=dag)
