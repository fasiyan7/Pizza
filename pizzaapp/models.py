from django.db import models

'''class Pizzeria(models.Model):
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)'''

class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    '''thumbnail_url = models.URLField()
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey(Pizzeria, on_delete=models.CASCADE)
    '''
    def __str__(self):
        return self.title
