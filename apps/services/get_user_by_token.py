# Django
from django.contrib.auth import get_user_model

# Rest-Framework
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()


def get_user_by_access_token(access_token_str):
    access_token_obj = AccessToken(access_token_str)
    user_id = access_token_obj['user_id']
    user = User.objects.get(id=user_id)

    response = {'user_id': user_id, 'user': user}
    return response
