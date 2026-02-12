# Django
from django.urls import path

# Project
from apps.main.comment.api.create import CommentCreateViewSet

comment_list_create = CommentCreateViewSet.as_view({'get': 'list', 'post': 'create'})
comment_detail = CommentCreateViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }
)

urlpatterns = [
    path('', comment_list_create, name='comment_list_create'),
    path('<uuid:pk>/', comment_detail, name='comment_detail_update_delete'),
]
