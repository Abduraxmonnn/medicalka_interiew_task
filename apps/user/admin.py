# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Project
from apps.user.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["username"]
    list_display = [
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
