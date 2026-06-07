from rest_framework.permissions import BasePermission, SAFE_METHODS
from projects.models import Contributor


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if hasattr(obj, 'author'):
            return obj.author == request.user
        return obj.project.author == request.user


class IsContributor(BasePermission):

    def has_object_permission(self, request, view, obj):
        project = getattr(obj, 'project', obj)
        return Contributor.objects.filter(project=project, user=request.user).exists()
