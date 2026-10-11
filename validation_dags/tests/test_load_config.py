from airflow_balancer.testing import pools
from airflow_config import load_config


class TestConfig:
    def test_load_config(self):
        with pools():
            config = load_config("config", "config")
            assert config
            assert config.extensions is not None
            assert "balancer" in config.extensions
            assert "libraries" in config.extensions
