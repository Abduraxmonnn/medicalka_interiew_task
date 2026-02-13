# Django
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework.filters import SearchFilter, OrderingFilter
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

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        'username',
        'full_name',
        'email',
    ]
    ordering_fields = ['username', 'full_name']
    ordering = ['-id']
