# Django
from rest_framework import routers

# Project
from apps.main.post.api import PostListOrCreateViewSet, PostDetailUpdateDestroyViewSet

router = routers.DefaultRouter()
router.register(r'', PostListOrCreateViewSet, basename='post_list_create')
router.register(r'', PostDetailUpdateDestroyViewSet, basename='post_detail_update_delete')

urlpatterns = [
    # path('<uuid:post_id>/comment/', include('apps.main.comment.urls')),
]

urlpatterns += router.urls
