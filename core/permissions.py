from rest_framework import permissions


class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(request, view)


class IsOwnerOrCreate(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit or view it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return True
        return obj.owner == request.user
