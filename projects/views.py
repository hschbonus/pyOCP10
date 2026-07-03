from rest_framework.viewsets import ModelViewSet
from projects.models import Comment, Issue, Project, Contributor
from projects.permissions import IsAuthor, IsContributor
from rest_framework.permissions import IsAuthenticated
from projects.serializers import CommentSerializer, ContributorSerializer, IssueSerializer, ProjectSerializer
from rest_framework.exceptions import PermissionDenied


class ProjectViewSet(ModelViewSet):

    def get_queryset(self):
        if self.action == 'list':
            return Project.objects.filter(contributor__user=self.request.user)
        return Project.objects.all()

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthor, IsContributor]

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(user=self.request.user, project=project)


class ContributorViewSet(ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Contributor.objects.filter(user=self.request.user)
        return Contributor.objects.all()

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsAuthor, IsContributor]

    def perform_create(self, serializer):
        project = serializer.validated_data['project']
        if project.author != self.request.user:
            raise PermissionDenied("Only the project author can add contributors.")
        serializer.save()


class IssueViewSet(ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Issue.objects.filter(project__contributor__user=self.request.user)
        return Issue.objects.all()

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthor, IsContributor]

    def perform_create(self, serializer):
        if 'project' in serializer.validated_data:
            project = serializer.validated_data['project']
            if not Contributor.objects.filter(project=project, user=self.request.user).exists():
                raise PermissionDenied("You must be a contributor of the project to create an issue.")
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Comment.objects.filter(issue__project__contributor__user=self.request.user)
        return Comment.objects.all()

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor, IsContributor]

    def perform_create(self, serializer):
        if 'issue' in serializer.validated_data:
            issue = serializer.validated_data['issue']
            if not Contributor.objects.filter(project=issue.project, user=self.request.user).exists():
                raise PermissionDenied("You must be a contributor of the project to create a comment.")
        serializer.save(author=self.request.user)
