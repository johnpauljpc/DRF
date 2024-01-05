from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user
    

class IsUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow actual user edit their information
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.username == request.user.username and obj.pk == request.user.pk