from rest_framework.permissions import BasePermission


class IsOwnerReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user