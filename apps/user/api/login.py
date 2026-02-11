# Reset-Framework
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Project
from apps.user.serializers.login import UserLogInSerializer


class UserLogInAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserLogInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        return Response(data, status=status.HTTP_200_OK)
