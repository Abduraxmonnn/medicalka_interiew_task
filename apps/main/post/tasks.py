# Python
from datetime import timedelta

# Django
from django.db import transaction
from django.utils import timezone

# Celery
from celery import shared_task

# Project
from apps.main.post.models import Post


@shared_task(name='apps.main.post.tasks.delete_expired_posts_task')
def delete_expired_posts_task(retention_days=30):
    cutoff_date = timezone.now() - timedelta(days=retention_days)

    # Use a transaction for safety and clarity
    with transaction.atomic():
        deleted_count, _ = (
            Post.objects.filter(created_at__lt=cutoff_date).delete()
        )
