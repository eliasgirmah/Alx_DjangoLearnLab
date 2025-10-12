from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: allow safe methods to anyone, allow write methods only for object owners.
    """

    def has_permission(self, request, view):
        # allow read-only for any, require authentication for unsafe methods
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for owner
        try:
            owner = getattr(obj, 'author')
        except AttributeError:
            return False
        return owner == request.user
