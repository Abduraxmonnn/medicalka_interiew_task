# Django
from django.contrib import admin

# Project
from apps.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ordering = ["username"]
    list_display = [
        "id",
        "username",
        "email",
        "full_name",
        "is_staff",
        "is_active",
        "is_verified",
        "created_at",
    ]
    search_fields = ["username", "email", "full_name"]
    readonly_fields = ["id", "created_at", "updated_at"]
