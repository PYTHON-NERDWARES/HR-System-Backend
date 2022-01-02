from rest_framework import permissions


class IsHROrEmployee(permissions.BasePermission):
    # def has_object_permission(self, request, view, obj):

    # hover over SAFE_METHODS to see which qualify
    # if request.method in permissions.SAFE_METHODS:
    #     return True

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.user.is_superuser
