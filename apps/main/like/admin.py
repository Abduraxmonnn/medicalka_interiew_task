# Django
from django.contrib import admin

# Project
from apps.main.like.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = [
        "id",
        "get_user_username",
        "get_post_title",
        "created_at",
    ]
    search_fields = ["author_id__username", "author_id__email", "post_id__title"]
    readonly_fields = ["id", "created_at"]

    def get_user_username(self, obj):
        return obj.author_id.username

    def get_post_title(self, obj):
        return obj.post_id.title
