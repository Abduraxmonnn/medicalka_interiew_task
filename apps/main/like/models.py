# Django
from django.db import models

# Project
from apps.main.post.models import Post
from apps.user.models import User


class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_id = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id.pk

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = (('user_id', 'post_id'),)
