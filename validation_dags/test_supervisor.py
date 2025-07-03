from datetime import timedelta

from airflow_config import DAG, load_config
from airflow_supervisor import SupervisorSSH

config = load_config("config", "config")
balancer_config = config.extensions["balancer"]
host = balancer_config.select_host(queue="primary")
port = balancer_config.select_port(name="test-supervisor-port")

with DAG(
    dag_id="lam-test-supervisor-noconfig",
    schedule=timedelta(days=1),
    config=config,
) as dag:
    supervisor = SupervisorSSH(dag=dag, cfg=config.extensions["supervisor"], host=host.override(username="airflow"), port=port)
