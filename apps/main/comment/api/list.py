# Rest-Framework
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

# Project
from apps.main.comment.models import Comment
from apps.main.comment.serializers.list import CommentListSerializer


class CommentListViewSet(ListModelMixin, GenericViewSet):
    queryset = Comment.objects.select_related('post_id', 'author_id')
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs.get('post_id'))
