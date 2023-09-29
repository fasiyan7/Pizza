from django.db import models
from user.models import UserProfile

class Pizzeria(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)
    def __str__(self):
        return self.owner.user.username
    
class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    thumbnail_url = models.URLField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey(Pizzeria, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

class Likes(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)