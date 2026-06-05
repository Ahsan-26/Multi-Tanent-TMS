from django.shortcuts import get_object_or_404
from organizations.models import Organization


class OrganizationResolverMixin:
    """
    Attaches organization object to view automatically
    based on URL parameter: org_id
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