from airflow_ha import Action, Result


def _get_count(**kwargs):
    return kwargs["dag_run"].conf.get("counter", 3) - 1


def _keep_counting(**kwargs):
    count = kwargs["task_instance"].xcom_pull(key="return_value", task_ids="lam-get-count")
    return (Result.PASS, Action.RETRIGGER) if count > 0 else (Result.PASS, Action.STOP) if count == 0 else (Result.FAIL, Action.STOP)
