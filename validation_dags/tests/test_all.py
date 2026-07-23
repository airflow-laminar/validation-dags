def test_all():
    from airflow_balancer.testing import pools

    with pools():
        import validation_dags.clean_dags
        import validation_dags.clean_journalctl
        import validation_dags.code_dags
        import validation_dags.dummy
        import validation_dags.dummy_foo
        import validation_dags.generate
        import validation_dags.succeed_on_rerun
        import validation_dags.succeed_on_rerun_foo
        import validation_dags.test_ha
        import validation_dags.test_ha_countdown
        import validation_dags.test_ha_countdown_foo
        import validation_dags.test_ha_foo
        import validation_dags.test_supervisor  # noqa: F401
