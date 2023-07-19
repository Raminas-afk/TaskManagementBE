from django.db import models

from . import TeamStatus
from tasks.models import Task
from users.models import User


class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    leaders = models.ManyToManyField(User, related_name='leading_teams')
    members = models.ManyToManyField(User, related_name='teams')
    tasks = models.ManyToManyField(Task, related_name='teams')
    status = models.CharField(choices=TeamStatus.CHOICES, max_length=20, default=TeamStatus.PUBLIC)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
