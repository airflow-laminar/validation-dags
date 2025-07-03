from datetime import datetime
from airflow.providers.standard.operators.python import PythonOperator

from airflow.models import DAG
# from airflow_config import DAG, load_config
from airflow_ha import HighAvailabilityOperator

# from validation_dags.test_ha_countdown_foo import _get_count, _keep_counting

# config = load_config("config", "config")


# with DAG(
#     dag_id="lam-test-ha-counter-noconfig",
#     config=config,
# ) as dag:
#     get_count = PythonOperator(task_id="lam-get-count", python_callable=_get_count, do_xcom_push=True)
#     keep_counting = HighAvailabilityOperator(
#         task_id="lam-ha",
#         timeout=30,
#         poke_interval=5,
#         python_callable=_keep_counting,
#         pass_trigger_kwargs={"conf": '{"counter": {{ ti.xcom_pull(key="return_value", task_ids="lam-get-count") }} }'},
#     )

#     get_count >> keep_counting

from validation_dags.test_ha_countdown_foo import _get_count, _keep_counting

with DAG(
    description="Test HA counter",
    schedule="0 0 * * *",
    start_date=datetime.fromisoformat("2025-01-01T00:00:00-04:56"),
    max_active_runs=1,
    catchup=False,
    tags=["lam", "test", "utility"],
    dag_id="lam-test-ha-counter-noconfig",
    default_args={
        "owner": "laminar",
        "email": ["dev@paine.nyc"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 0,
        "depends_on_past": False,
    },
) as dag:
    # lam_get_count = PythonOperator(task_id="lam_get_count", python_callable=_get_count, do_xcom_push=True)
    lam_get_count = PythonOperator(task_id="lam-get-count", python_callable=_get_count, do_xcom_push=True)
    # lam_ha = HighAvailabilityOperator(
    #     poke_interval=5.0,
    #     timeout=30.0,
    #     python_callable=_keep_counting,
    #     pass_trigger_kwargs={"conf": '{"counter": {{ ti.xcom_pull(key="return_value", task_ids="lam_get_count") }} }'},
    #     # pass_trigger_kwargs={"conf": '{"counter": {{ ti.xcom_pull(key="return_value", task_ids="lam-get-count") }} }'},
    #     task_id="lam_ha",
    #     dag=dag,
    # )
    lam_ha = HighAvailabilityOperator(
        task_id="lam-ha",
        timeout=30,
        poke_interval=5,
        python_callable=_keep_counting,
        pass_trigger_kwargs={"conf": '{"counter": {{ ti.xcom_pull(key="return_value", task_ids="lam-get-count") }} }'},
    )
    lam_get_count >> lam_ha
