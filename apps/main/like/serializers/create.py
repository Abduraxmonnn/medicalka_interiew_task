# Django
from django.contrib.auth import get_user_model

# Rest-Framework
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

# Project
from apps.main.like.models import Like
from apps.main.post.models import Post

User = get_user_model()


class LikeCreateDeleteSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Like
        fields = "__all__"

    def validate(self, attrs):
        """
        Validate the combination of author_id and post_id
        """
        author = attrs.get("author_id")
        post = attrs.get("post_id")

        if Like.is_post_owner(author, post):
            raise PermissionDenied("Post owner cannot like their own post.")

        if Like.is_already_liked(author, post):
            raise serializers.ValidationError("User already liked this Post!")

        return attrs
