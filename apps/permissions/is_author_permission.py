from rest_framework.permissions import BasePermission


class IsPostAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author_id == request.user
