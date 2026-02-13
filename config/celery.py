import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
from celery.schedules import schedule

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("medicalka")
app.config_from_object("django.conf:settings", namespace='CELERY')
app.autodiscover_tasks()
app.conf.timezone = "Asia/Tashkent"

app.conf.beat_schedule = {
    'delete-expired-users-every-day-midnight': {
        'task': 'apps.user.tasks.delete_expired_users_task',
        'schedule': crontab(minute=0, hour=0, day_of_week='sunday')
    },

    'delete-expired-posts-every-30-days-midnight': {
        'task': 'apps.main.post.tasks.delete_expired_posts_task',
        'schedule': schedule(run_every=timedelta(days=30)),
    }
}
