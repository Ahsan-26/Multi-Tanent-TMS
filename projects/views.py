from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.mixins.organization_resolver import OrganizationResolverMixin
from memberships.permissions import IsOrgMember
from .models import Project
from .serializers import ProjectSerializer


class ProjectListCreateView(OrganizationResolverMixin, APIView):
    permission_classes = [IsAuthenticated, IsOrgMember]

    def get(self, request, org_id):
        projects = Project.objects.filter(
            organization=self.organization
        )

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, org_id):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        project = serializer.save(
            organization=self.organization
        )

        return Response(ProjectSerializer(project).data)