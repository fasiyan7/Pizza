from django.db import models
from .models import UserProfile

class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    def __str__(self):
        return self.title
