# Rest-Framework
from rest_framework import serializers


class UserVerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.IntegerField()
