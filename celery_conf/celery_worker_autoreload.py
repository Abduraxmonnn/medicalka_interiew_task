# celery_worker_autoreload.py
import os
import subprocess
from django.utils.autoreload import run_with_reloader

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


def run_celery_worker():
    """
    Runs Celery worker with autoreload support.
    Useful during development — restarts when code changes.
    """
    worker = subprocess.Popen([
        "celery",
        "-A", "medicalka",
        "worker",
        "--loglevel=info",
        "--pool=solo",  # required for autoreload
    ])

    try:
        worker.wait()
    except KeyboardInterrupt:
        worker.terminate()


if __name__ == "__main__":
    run_with_reloader(run_celery_worker)
