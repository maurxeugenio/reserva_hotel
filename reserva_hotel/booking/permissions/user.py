from rest_framework import permissions

class IsOwnerOrEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
    
        if request.user and request.user.is_authenticated:
            if request.user.is_owner or request.user.is_employee:
                return True

        return False