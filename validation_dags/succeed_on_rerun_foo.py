import os
from tempfile import gettempdir


def _fail_on_first_run(**kwargs):
    tempfile = gettempdir() + f"/{kwargs['dag_run'].run_id}.txt"
    if os.path.exists(tempfile):
        os.remove(tempfile)
        return
    open(tempfile, "w").close()
    raise RuntimeError(f"Task failed on first run. Please re-run the DAG: {kwargs['dag_run'].run_id}")
