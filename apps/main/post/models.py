# Django
import uuid

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

User = get_user_model()


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    author_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    title = models.CharField(max_length=255, validators=[MinLengthValidator(5)])
    content = models.TextField(max_length=10_000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
