# Django
from django.contrib.auth import get_user_model

# Rest-Framework
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# Project
from apps.main.comment.serializers.list import CommentListSerializer
from apps.main.post.models import Post

User = get_user_model()


class PostListOrCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author_username = serializers.CharField(write_only=True)
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        title = validated_data.get('title', None)
        author_username = validated_data.pop('author_username', None)

        if None in [title, author_username]:
            raise ValidationError("title and author_username are required.")

        try:
            user_obj = User.objects.get(username=author_username)
        except User.DoesNotExist:
            raise serializers.ValidationError({"author_username": "User not found"})

        return Post.objects.create(author_id=user_obj, **validated_data)
