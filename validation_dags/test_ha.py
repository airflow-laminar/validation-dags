from datetime import time

from airflow.providers.standard.operators.python import PythonOperator
from airflow_config import DAG, load_config
from airflow_ha import HighAvailabilityOperator
from airflow_pydantic import fail

from validation_dags.test_ha_foo import _choose, _pre

config = load_config("config", "config")

with DAG(
    dag_id="lam-test-high-availability-noconfig",
    config=config,
):
    ha = HighAvailabilityOperator(
        task_id="ha",
        runtime=120,
        maxretrigger=2,
        endtime=time(23, 0),
        timeout=1000,
        poke_interval=10,
        python_callable=_choose,
    )

    pre = PythonOperator(task_id="lam-pre", python_callable=_pre)
    pre >> ha

    retrigger_fail = PythonOperator(task_id="lam-retrigger_fail", python_callable=_pre)
    ha.retrigger_fail >> retrigger_fail

    stop_fail = PythonOperator(task_id="lam-stop_fail", python_callable=fail, trigger_rule="all_failed")
    ha.stop_fail >> stop_fail

    retrigger_pass = PythonOperator(task_id="lam-retrigger_pass", python_callable=_pre)
    ha.retrigger_pass >> retrigger_pass

    stop_pass = PythonOperator(task_id="lam-stop_pass", python_callable=_pre)
    ha.stop_pass >> stop_pass
