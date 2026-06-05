from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import OrganizationSerializer
from .services import create_organization


class OrganizationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        org = create_organization(
            user=request.user,
            validated_data=serializer.validated_data
        )

        return Response({
            "success": True,
            "data": OrganizationSerializer(org).data
        })