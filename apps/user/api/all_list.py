# Django
from django.contrib.auth import get_user_model

# Rest-Framework
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

User = get_user_model()

# Project
from apps.user.serializers.all_list import UserAllListSerializer


class UserAllListViewSet(ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserAllListSerializer
    permission_classes = [AllowAny]
    http_method_names = ('get',)
