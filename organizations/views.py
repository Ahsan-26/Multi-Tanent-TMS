from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Organization
from memberships.models import Membership

class OrganizationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        name = request.data.get("name")

        org = Organization.objects.create(name=name)

        # AUTO: creator becomes admin
        Membership.objects.create(
            user=request.user,
            organization=org,
            role="admin"
        )

        return Response({
            "id": org.id,
            "name": org.name
        })