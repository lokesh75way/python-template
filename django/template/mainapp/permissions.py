from rest_framework import permissions

# 4.4 Authentication & Permissions (Custom permissions)
class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow managers into the view.
    """
    def has_permission(self, request, view):
        # Allow read-only for authenticated
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        # Write permissions are only allowed to managers
        return request.user.groups.filter(name='Manager').exists()
