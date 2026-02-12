# Rest-Framework
from django.contrib.auth import get_user_model
from rest_framework import serializers

# Project
from apps.main.post.models import Post
from apps.main.comment.models import Comment

User = get_user_model()


class PostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'full_name',
            'is_verified'
        ]


class PostDetailUpdateDestroySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    comments = PostCommentsSerializer(many=True, read_only=True)
    author_id = PostAuthorSerializer(read_only=True)
    new_author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Post
        fields = '__all__'

    def update(self, instance, validated_data):
        new_author = validated_data.pop('new_author_id', None)
        if new_author:
            instance.author_id = new_author

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
