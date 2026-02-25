from rest_framework import permissions


class IsModerators(permissions.BasePermission):
    """Проверка: является ли пользователь Модератором."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderators").exists()


class IsOwner(permissions.BasePermission):
    """Проверка: является ли пользователь Владельцем"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
