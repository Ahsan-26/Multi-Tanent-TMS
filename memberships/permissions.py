from rest_framework.permissions import BasePermission
from .services import get_membership


class IsOrgMember(BasePermission):
    def has_permission(self, request, view):
        organization = getattr(view, "organization", None)

        if not request.user or not request.user.is_authenticated:
            return False

        if not organization:
            return False

        return get_membership(request.user, organization) is not None


class IsOrgAdmin(BasePermission):
    def has_permission(self, request, view):
        organization = getattr(view, "organization", None)

        membership = get_membership(request.user, organization)

        if not membership:
            return False

        return membership.role == "admin"


class IsOrgAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        organization = getattr(view, "organization", None)

        membership = get_membership(request.user, organization)

        if not membership:
            return False

        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        return membership.role == "admin"