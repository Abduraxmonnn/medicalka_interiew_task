import os
import subprocess
import sys
from pathlib import Path
from django.utils.autoreload import run_with_reloader

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))


def run_celery_worker():
    """
    Runs Celery worker with autoreload support.
    Useful during development — restarts when code changes.
    """
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{BASE_DIR}{os.pathsep}{env.get('PYTHONPATH', '')}".rstrip(os.pathsep)

    worker = subprocess.Popen([
        sys.executable,
        "-m",
        "celery",
        "-A",
        "config.celery:app",
        "worker",
        "--loglevel=info",
        "--pool=solo",
    ], cwd=BASE_DIR, env=env)

    try:
        worker.wait()
    except KeyboardInterrupt:
        worker.terminate()


if __name__ == "__main__":
    run_with_reloader(run_celery_worker)
