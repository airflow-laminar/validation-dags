from airflow_config import load_config

config = load_config("config", "config")
config.generate_in_mem(placeholder_dag_id="lam-generate-dags")
