# Rest-Framework
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin

# Project
from apps.main.post.models import Post
from apps.main.post.serializers.list_and_create import PostListOrCreateSerializer


class PostListOrCreateViewSet(ListModelMixin, GenericViewSet):
    queryset = Post.objects.select_related('author_id')
    serializer_class = PostListOrCreateSerializer
    permission_classes = [AllowAny]
    http_method_names = ('get', )
