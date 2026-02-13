# Rest-Framework
from rest_framework import routers

# Project
from apps.main.like.api import LikeCreateDeleteViewSet

router = routers.DefaultRouter()
router.register(r'', LikeCreateDeleteViewSet, basename='like_delete_create')

urlpatterns = router.urls
