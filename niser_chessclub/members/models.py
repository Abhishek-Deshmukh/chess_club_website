from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100, blank=True)
    designation = models.CharField(max_length=20, default="Player",choices=(
        ('player', 'Player'),
        ('captain', 'Captain'),
        ('v_captain', 'Vice_Captain'),
    ))
    school = models.CharField(max_length=10, default="FY",choices=(
        ('fy', 'FY'),
        ('sbs', 'SBS'),
        ('sps', 'SPS'),
        ('scs', 'SCS'),
        ('sms', 'SMS'),
    ))
    description = models.CharField(max_length=10000, default=" ")
    image = models.ImageField(upload_to='images/', blank=True)

def __str__(self):
    return self.name
