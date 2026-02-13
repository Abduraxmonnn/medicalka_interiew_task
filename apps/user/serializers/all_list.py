# Django
from django.contrib.auth import get_user_model

# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.post.models import Post

User = get_user_model()


class UserAllListPostSerializer(serializers.ModelSerializer):
    likes_post = serializers.SerializerMethodField()
    likes_total = serializers.SerializerMethodField()
    comments_total = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'author_id',
            'title',
            'content',
            'likes_post',
            'likes_total',
            'comments_total'
        ]

    def get_likes_post(self, obj):
        return list(obj.likes_post.values_list('author_id', flat=True))

    def get_likes_total(self, obj):
        return obj.likes_post.count()

    def get_comments_total(self, obj):
        return obj.comments.count()


class UserAllListSerializer(serializers.ModelSerializer):
    posts = UserAllListPostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'posts'
        ]
