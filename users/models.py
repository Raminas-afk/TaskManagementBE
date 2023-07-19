from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    icon = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.username
