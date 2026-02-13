# Python
import random

# Django
from django.contrib.auth import get_user_model

# Reset-Framework
from rest_framework import serializers

# Project
from apps.user.services.send_otp import send_otp_code_via_email

User = get_user_model()
OTP_CODE = random.randint(100000, 999999)


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    message_language = serializers.CharField(max_length=2, write_only=True, required=False)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'full_name', 'message_language', 'access', 'refresh']

    def create(self, validated_data):
        request = self.context.get('request')
        user = User.objects.create_user(**validated_data, otp_code=OTP_CODE, is_verified=False)
        is_fake_verify = False
        is_emailed = False

        if request:
            fake_verify_str = request.query_params.get('fake_verify', None)
            if fake_verify_str is not None:
                is_fake_verify = fake_verify_str.lower() in ['true', '1', 'yes']

        if not is_fake_verify:
            is_emailed: bool = send_otp_code_via_email(
                user.email,
                OTP_CODE,
                lang=str(validated_data.get('message_language', 'EN')).upper()
            )
        else:
            user.otp_code = OTP_CODE
            user.save()

        return {
            "email": user.email,
            "username": user.username,
            "full_name": user.full_name,
            "is_sent_otp": is_emailed,
            "otp_code": OTP_CODE
        }
