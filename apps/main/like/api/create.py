# Rest-Framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin

# Project
from apps.main.like.models import Like
from apps.main.like.serializers.create import LikeCreateDeleteSerializer
from apps.permissions.is_author_permission import IsAuthorOrReadOnly


class LikeCreateDeleteViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Like.objects.select_related('post_id', 'author_id')
    serializer_class = LikeCreateDeleteSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "status": "success",
            "data": serializer.data,
        }, status=201)
