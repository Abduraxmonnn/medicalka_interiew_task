# Reset-Framework
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

# Project
from apps.user.serializers.update import UserUpdateSerializer


class UserUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request):
        serializer = UserUpdateSerializer(
            instance=request.user,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        return Response(data, status=status.HTTP_200_OK)
