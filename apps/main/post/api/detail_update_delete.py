# Rest-Framework
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin

# Project
from apps.main.post.models import Post
from apps.main.post.serializers.detail_update_delete import PostDetailUpdateDestroySerializer
from apps.permissions.is_author_permission import IsAuthorOrReadOnly


class PostDetailUpdateDestroyViewSet(RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Post.objects.select_related('author_id').prefetch_related('comments')
    serializer_class = PostDetailUpdateDestroySerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAuthorOrReadOnly()]

        return [IsAuthenticated()]
