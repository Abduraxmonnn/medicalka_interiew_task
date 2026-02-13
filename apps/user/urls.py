# Django
from django.urls import path

# Project
from apps.user.api import UserRegisterAPIView, UserLogInAPIView, UserMeAPIView, UserUpdateAPIView, UserAllListViewSet

urlpatterns = [
    path('auth/register/', UserRegisterAPIView.as_view(), name='user_register'),
    path('auth/login/', UserLogInAPIView.as_view(), name='user_login'),
    path('auth/me/', UserMeAPIView.as_view(), name='user_me'),
    path('users/me/', UserUpdateAPIView.as_view(), name='user_update'),
    path('all/', UserAllListViewSet.as_view({'get': 'list'}), name='user_all_list'),
]
