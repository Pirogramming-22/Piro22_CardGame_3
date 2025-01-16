from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    score = models.IntegerField(default=0)
    email = models.EmailField()

    def __str__(self):
        return self.username
