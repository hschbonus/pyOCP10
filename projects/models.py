from django.db import models
import uuid


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=[
        ('back-end', 'Back-End'),
        ('front-end', 'Front-End'),
        ('iOS', 'iOS'),
        ('android', 'Android'),
    ])
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contributor(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user.username} - {self.project.name}"


class Issue(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    tag = models.CharField(max_length=20, choices=[
        ('bug', 'BUG'),
        ('feature', 'FEATURE'),
        ('task', 'TASK'),
    ])
    priority = models.CharField(max_length=20, choices=[
        ('low', 'LOW'),
        ('medium', 'MEDIUM'),
        ('high', 'HIGH'),
    ])
    status = models.CharField(max_length=20, choices=[
        ('to do', 'TO DO'),
        ('in progress', 'IN PROGRESS'),
        ('done', 'DONE'),
    ], default='to do')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='issues_authored'
    )
    assigned_to = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='issues_assigned',
        null=True,
        blank=True
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    description = models.TextField()
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    @property
    def project(self):
        return self.issue.project

    def __str__(self):
        return f"Comment by {self.author.username} on {self.issue.name}"
