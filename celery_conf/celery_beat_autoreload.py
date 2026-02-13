# celery_beat_autoreload.py
import os
import subprocess
from django.utils.autoreload import run_with_reloader

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


def run_celery_beat():
    """
    Runs Celery beat (scheduler) with autoreload support.
    Useful during development — restarts when code changes.
    """
    beat = subprocess.Popen([
        "celery",
        "-A", "medicalka",
        "beat",
        "--loglevel=info",
        "--schedule", os.path.join(os.path.dirname(__file__), "celerybeat-schedule"),
    ])

    try:
        beat.wait()
    except KeyboardInterrupt:
        beat.terminate()


if __name__ == "__main__":
    run_with_reloader(run_celery_beat)
