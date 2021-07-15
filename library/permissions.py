from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            if request.user.is_superuser:
                return True
            return False
        return True
