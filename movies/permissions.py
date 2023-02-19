from rest_framework import permissions


class MoviesPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_employee
        return request.method in permissions.SAFE_METHODS


class MoviesDetailsPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.is_employee
        return request.method in permissions.SAFE_METHODS
