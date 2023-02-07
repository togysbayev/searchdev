from rest_framework import permissions

class CanViewHistoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            print(f"Permission: {request.user.has_perm('developers.view_history')}")
            return request.user.has_perm('developers.view_history')
        return False
    
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    
class IsOwnerOfProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.id == request.user.profile.id
