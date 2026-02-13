# Rest-Framework
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

# Project
from apps.main.comment.models import Comment
from apps.main.comment.serializers.create import CommentCreateSerializer
from apps.main.comment.serializers.list import CommentListSerializer
from apps.permissions.is_author_permission import IsAuthorOrReadOnly


class CommentCreateViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Comment.objects.select_related('post_id', 'author_id')

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs.get('post_id'))

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CommentListSerializer
        return CommentCreateSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAuthorOrReadOnly()]
        return [AllowAny()]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {
                "status": "success",
                "message": "deleted successfully",
            },
            status=status.HTTP_204_NO_CONTENT
        )
