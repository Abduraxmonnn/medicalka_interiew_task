# Python
from datetime import timedelta

# Django
from django.db import transaction
from django.utils import timezone
from django.contrib.auth import get_user_model

# Celery
from celery import shared_task

User = get_user_model()


@shared_task(name='apps.main.user.tasks.delete_expired_users_task')
def delete_expired_users_task(retention_days=1):
    cutoff_date = timezone.now() - timedelta(days=retention_days)

    # Use a transaction for safety and clarity
    with transaction.atomic():
        deleted_count, _ = (
            User.objects.filter(is_verified=False, created_at__lt=cutoff_date).delete()
        )
