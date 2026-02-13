# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.main.post.models import Post
from apps.main.post.serializers.list_and_create import PostListOrCreateSerializer


class PostListOrCreateViewSet(ListModelMixin, GenericViewSet):
    queryset = Post.objects.select_related('author_id')
    serializer_class = PostListOrCreateSerializer
    permission_classes = [AllowAny]
    http_method_names = ('get',)

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        'title',
        'content',
    ]
    ordering_fields = ['created_at']
    ordering = ['-id']
