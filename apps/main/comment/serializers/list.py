# Django
from django.contrib.auth import get_user_model

# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.comment.models import Comment
from apps.main.post.models import Post

User = get_user_model()


class CommentPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'full_name',
            'is_verified'
        ]


class CommentListSerializer(serializers.ModelSerializer):
    post_id = CommentPostListSerializer()
    author_id = CommentAuthorSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
