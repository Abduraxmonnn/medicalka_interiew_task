import os
import subprocess
import sys
from pathlib import Path
from django.utils.autoreload import run_with_reloader

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
BASE_DIR = Path(__file__).resolve().parent.parent
SCHEDULE_FILE = Path(__file__).resolve().parent / "celerybeat-schedule"
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))


def run_celery_beat():
    """
    Runs Celery beat (scheduler) with autoreload support.
    Useful during development — restarts when code changes.
    """
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{BASE_DIR}{os.pathsep}{env.get('PYTHONPATH', '')}".rstrip(os.pathsep)

    beat = subprocess.Popen([
        sys.executable,
        "-m",
        "celery",
        "-A",
        "config.celery:app",
        "beat",
        "--loglevel=info",
        "--schedule",
        str(SCHEDULE_FILE),
    ], cwd=BASE_DIR, env=env)

    try:
        beat.wait()
    except KeyboardInterrupt:
        beat.terminate()


if __name__ == "__main__":
    run_with_reloader(run_celery_beat)
