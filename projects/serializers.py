from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from projects.models import Comment, Contributor, Issue, Project


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'type', 'author', 'created_time']

    author = serializers.PrimaryKeyRelatedField(read_only=True)
    created_time = serializers.DateTimeField(read_only=True)


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user_id', 'project_id']


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            'id', 'name', 'description', 'tag', 'priority', 'status',
            'project', 'author', 'assigned_to', 'created_time'
        ]

    author = serializers.PrimaryKeyRelatedField(read_only=True)
    created_time = serializers.DateTimeField(read_only=True)


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'description', 'uuid', 'issue', 'author', 'created_time']

    author = serializers.PrimaryKeyRelatedField(read_only=True)
    uuid = serializers.UUIDField(read_only=True)
    created_time = serializers.DateTimeField(read_only=True)
