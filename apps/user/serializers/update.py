# Reset-Framework
from rest_framework import serializers

# Project
from apps.user.models import User


class UserUpdateSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    full_name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['email', 'username', 'full_name']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return {
            "email": instance.email,
            "username": instance.username,
            "full_name": instance.full_name,
        }
