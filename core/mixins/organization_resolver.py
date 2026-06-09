from django.shortcuts import get_object_or_404
from organizations.models import Organization


class OrganizationResolverMixin:
    """
    Resolves organization from URL (org_id)
    and attaches it to the view instance.
    """

    def dispatch(self, request, *args, **kwargs):
        org_id = kwargs.get("org_id")

        if org_id:
            self.organization = get_object_or_404(
                Organization,
                id=org_id
            )
        else:
            self.organization = None

        return super().dispatch(request, *args, **kwargs)