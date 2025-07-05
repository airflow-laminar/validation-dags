def test_all():
    from airflow_balancer.testing import pools

    with pools():
        import validation_dags.clean_dags  # noqa: F401
        import validation_dags.clean_journalctl  # noqa: F401
        import validation_dags.code_dags  # noqa: F401
        import validation_dags.dummy  # noqa: F401
        import validation_dags.dummy_foo  # noqa: F401
        import validation_dags.generate  # noqa: F401
        import validation_dags.succeed_on_rerun  # noqa: F401
        import validation_dags.succeed_on_rerun_foo  # noqa: F401
        import validation_dags.test_ha  # noqa: F401
        import validation_dags.test_ha_countdown  # noqa: F401
        import validation_dags.test_ha_countdown_foo  # noqa: F401
        import validation_dags.test_ha_foo  # noqa: F401
        import validation_dags.test_supervisor  # noqa: F401
