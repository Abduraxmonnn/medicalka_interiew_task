# Django
import uuid

from django.contrib.auth import get_user_model

# Project
from apps.main.post.models import Post

User = get_user_model()


def is_post_likeable_service(
        author_id: uuid.uuid4,
        post_id: uuid.uuid4,
        user_obj: User.objects,
        post_obj: Post.objects
):
    user_obj.get(id=author_id)
    post_obj.get(id=post_id)

    if user_obj == post_obj.author_id:
        return True

    return False
