# Django
from django.contrib.auth import authenticate

# Reset-Framework
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# Project
from apps.user.models import User


class UserMeSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, min_length=8)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = User.objects.get(username=username, password=password)

            if user is None:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Must include username and password")

        self.user = user
        return data

    def create(self, validated_data):
        user = self.user
        refresh = RefreshToken.for_user(user)

        return {
            "email": user.email,
            "username": user.username,
            "full_name": user.full_name,
            "is_verified": user.is_verified,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
