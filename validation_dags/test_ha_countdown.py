from airflow.operators.python import PythonOperator
from airflow_config import DAG, load_config
from airflow_ha import HighAvailabilityOperator

from validation_dags.test_ha_countdown_foo import _get_count, _keep_counting

config = load_config("config", "config")


with DAG(
    dag_id="lam-test-ha-counter-noconfig",
    config=config,
) as dag:
    get_count = PythonOperator(task_id="lam-get-count", python_callable=_get_count, do_xcom_push=True)
    keep_counting = HighAvailabilityOperator(
        task_id="lam-ha",
        timeout=30,
        poke_interval=5,
        python_callable=_keep_counting,
        pass_trigger_kwargs={"conf": '{"counter": {{ ti.xcom_pull(key="return_value", task_ids="lam-get-count") }} }'},
    )

    get_count >> keep_counting
