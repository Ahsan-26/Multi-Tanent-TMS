from .models import Membership

def get_membership(user, organization):
    return Membership.objects.filter(
        user=user,
        organization=organization
    ).first()