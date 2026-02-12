# Django
from django.contrib.auth import get_user_model

# Rest-Framework
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# Project
from apps.main.comment.models import Comment
from apps.main.post.models import Post

User = get_user_model()


class CommentCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    author_id = serializers.UUIDField(write_only=True)
    post_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author_id', 'post_id', 'content']

    def create(self, validated_data):
        post_id = validated_data.pop('post_id', None)
        author_id = validated_data.pop('author_id', None)

        if None in [post_id, author_id]:
            raise ValidationError("post_id and author_id are required.")

        try:
            user_obj = User.objects.get(id=author_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"author_id": "User not found"})

        try:
            post_obj = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise serializers.ValidationError({"post_id": "Post not found"})

        return Comment.objects.create(author_id=user_obj, post_id=post_obj, **validated_data)
