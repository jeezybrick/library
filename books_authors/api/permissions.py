from rest_framework import permissions


class IsAuthenticatedReadOnly(permissions.BasePermission):
    """
    Permission to only allow users that authenticated to see
    the content, allowed methods: GET, HEAD, OPTIONS
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated() and request.method in permissions.SAFE_METHODS:
            return True
