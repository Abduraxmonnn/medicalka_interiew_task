# Django
from django.db import models
from django.contrib.auth import get_user_model

# Project
from apps.main.post.models import Post

User = get_user_model()


class Like(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='likes_author')
    post_id = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='likes_post')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post_id.pk)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = (('author_id', 'post_id'),)

    @classmethod
    def is_already_liked(cls, user, post) -> bool:
        return cls.objects.filter(author_id=user, post_id=post).exists()

    @classmethod
    def is_post_owner(cls, user, post) -> bool:
        return user == post.author_id
