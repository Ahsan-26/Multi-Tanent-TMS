from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

from .models import Membership


class IsAuthenticatedAndOrgMember(BasePermission):
    """
    Ensures:
    1. User is authenticated
    2. User belongs to the organization
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        organization = getattr(view, "organization", None)

        if not organization:
            return False

        return Membership.objects.filter(
            user=request.user,
            organization=organization
        ).exists()


class IsOrgAdmin(BasePermission):
    """
    Allows only admins of the organization
    """

    def has_permission(self, request, view):
        organization = getattr(view, "organization", None)

        if not organization:
            return False

        membership = Membership.objects.filter(
            user=request.user,
            organization=organization
        ).first()

        if not membership:
            return False

        return membership.role == "admin"


class IsOrgMember(BasePermission):
    """
    Basic membership check (any role allowed)
    """

    def has_permission(self, request, view):
        organization = getattr(view, "organization", None)

        if not organization:
            return False

        return Membership.objects.filter(
            user=request.user,
            organization=organization
        ).exists()


class IsOrgAdminOrReadOnly(BasePermission):
    """
    Admin can write, others can only read
    """

    def has_permission(self, request, view):
        organization = getattr(view, "organization", None)

        if not organization:
            return False

        membership = Membership.objects.filter(
            user=request.user,
            organization=organization
        ).first()

        if not membership:
            return False

        # read-only methods allowed for all members
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        return membership.role == "admin"