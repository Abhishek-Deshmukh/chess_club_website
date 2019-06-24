from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'designation', 'email')
    list_per_page = 20
    search_fields = ('name', 'email')
    list_filter = ('school',)

# Register or Unregister your models here.
admin.site.register(Member, MemberAdmin)
admin.site.unregister(Group)
