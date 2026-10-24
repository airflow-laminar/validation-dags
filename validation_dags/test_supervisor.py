from datetime import timedelta

from airflow_balancer import BalancerConfiguration
from airflow_config import DAG, load_config
from airflow_supervisor import SupervisorSSH, SupervisorSSHAirflowConfiguration

config = load_config("config", "config")
assert config.extensions is not None
balancer_config = config.extensions["balancer"]
assert isinstance(balancer_config, BalancerConfiguration)
supervisor_config = config.extensions["supervisor"]
assert isinstance(supervisor_config, SupervisorSSHAirflowConfiguration)
host = balancer_config.select_host(queue="nuc2")
port = balancer_config.select_port(name="test-supervisor-port")

with DAG(
    dag_id="lam-test-supervisor-noconfig",
    schedule=timedelta(days=1),
    config=config,
) as dag:
    supervisor = SupervisorSSH(dag=dag, cfg=supervisor_config, host=host.override(username="airflow"), port=port)
