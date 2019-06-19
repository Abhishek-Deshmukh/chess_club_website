from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Member

# Register your models here.
admin.site.register(Member)
admin.site.unregister(Group)
