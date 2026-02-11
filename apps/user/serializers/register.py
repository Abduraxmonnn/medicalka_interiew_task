# Reset-Framework
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# Project
from apps.user.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'full_name', 'access', 'refresh']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, is_verified=False)

        refresh = RefreshToken.for_user(user)

        return {
            "email": user.email,
            "username": user.username,
            "full_name": user.full_name,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
