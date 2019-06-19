from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True)
    date = models.DateField(auto_now_add=True)

def __str__(self):
    return self.date
