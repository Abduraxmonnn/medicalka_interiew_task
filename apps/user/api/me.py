# Rest-Framework
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

# Project
from apps.services import get_user_by_access_token
from apps.validations.token_validate import auth_token_validate


class UserMeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        token = auth_token_validate(request)

        if 'error' in token:
            return Response(token.get('error', {}), token.get('status_code', 401))

        user_data = get_user_by_access_token(token.get('token'))

        return Response({
            "user_id": user_data['user_id'],
            "username": user_data['user'].username,
            "email": user_data['user'].email,
            "full_name": user_data['user'].full_name,
            "is_verified": user_data['user'].is_verified
        })
