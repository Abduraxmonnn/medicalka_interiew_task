# Django
import uuid

from django.db import models

# Project
from apps.main.post.models import Post
from apps.user.models import User


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    author_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=2_000)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id.pk

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'
