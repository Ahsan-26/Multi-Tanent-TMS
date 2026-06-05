from rest_framework.exceptions import PermissionDenied
from memberships.models import Membership

def check_membership(user, organization):
    if not Membership.objects.filter(user=user, organization=organization).exists():
        raise PermissionDenied("You are not part of this organization")