# Django
from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.user.urls')),
    path('posts/', include('apps.main.post.urls')),
    path('posts/<uuid:post_id>/comment/', include('apps.main.comment.urls')),
]
