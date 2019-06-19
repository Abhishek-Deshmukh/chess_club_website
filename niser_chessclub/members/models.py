from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    description = models.CharField(max_length=10000, default=" ")
    image = models.ImageField(upload_to='images/', blank=True)

def __str__(self):
    return self.name
