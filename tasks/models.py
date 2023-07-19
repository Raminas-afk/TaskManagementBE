from django.db import models
from . import TaskStatus

# Create your models here.


class Task(models.Model):
    # assignee = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tasks')
    # proposer = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='assigned_tasks')
    # Uncomment and migrate when Custom user model is implemented
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(choices=TaskStatus.CHOICES, max_length=20, default=TaskStatus.TODO)
    is_completed = models.BooleanField(default=False, blank=True, null=True)
    priority = models.IntegerField(default=0, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
