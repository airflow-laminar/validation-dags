from random import choice

from airflow_ha import Action, Result


def _pre(**kwargs):
    return "test"


def _choose(**kwargs):
    return choice(
        (
            (Result.PASS, Action.CONTINUE),
            (Result.PASS, Action.RETRIGGER),
            # (Result.PASS, Action.STOP),
            # (Result.FAIL, Action.CONTINUE),
            # (Result.FAIL, Action.RETRIGGER),
            # (Result.FAIL, Action.STOP),
        )
    )
