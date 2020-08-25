from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check users is trying to edit their own id"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to update there own status """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
