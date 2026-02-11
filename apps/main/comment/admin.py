# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Project
from apps.main.comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = [
        "id",
        "get_author_username",
        "get_post_title",
        "created_at",
    ]
    search_fields = ["author_id__username", "author_id__email", "post_id__title"]
    readonly_fields = ["id", "created_at"]

    def get_author_username(self, obj):
        return obj.user_id.username

    def get_post_title(self, obj):
        return obj.post_id.title
