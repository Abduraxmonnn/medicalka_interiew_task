# Python
import datetime

from django.db import transaction
# Django
from django.utils import timezone
from django.contrib.auth import get_user_model

# Rest-Framework
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response
from rest_framework_simplejwt.tokens import RefreshToken

# Project
from apps.user.serializers.accout_verify import UserVerifyOtpSerializer

User = get_user_model()


# Code from 3 years ago. xD ;)
class UserVerifyOTPAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserVerifyOtpSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        email = serializer.data['email']
        otp = serializer.data['otp']
        user = User.objects.filter(email__iexact=email)

        with transaction.atomic():
            if user.exists():
                if user.first().is_verified is True:
                    return Response({
                        "message": "User exists",
                        'data': serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)

            last_user = user.last()
            if last_user.otp_code != otp:
                return Response({
                    'message': 'OTP is wrong',
                    'data': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

            user_ex_time = last_user.created_at + datetime.timedelta(minutes=5)
            if user_ex_time <= timezone.now() is False:
                return Response({
                    'message': 'Verified code has expired',
                    'data': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            last_user.is_verified = True
            last_user.is_active = True
            last_user.save()

            refresh = RefreshToken.for_user(last_user)

        return Response({
            'message': 'Account is verified',
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            'data': serializer.data,
        }, status=status.HTTP_200_OK)
