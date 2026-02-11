# Django
from django.contrib import admin

# Project
from apps.main.post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = [
        "id",
        "title",
        "created_at",
    ]
    search_fields = ["title", "author_id__username", "author_id__email"]
    readonly_fields = ["id", "created_at", "updated_at"]
