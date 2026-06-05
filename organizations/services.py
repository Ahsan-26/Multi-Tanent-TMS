from .models import Organization


def create_organization(user, validated_data):
    org = Organization.objects.create(
        name=validated_data['name']
    )

    # In real system: also create membership
    from memberships.models import Membership

    Membership.objects.create(
        user=user,
        organization=org,
        role='admin'
    )

    return org