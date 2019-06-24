from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time')
    list_per_page = 20
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)

# Register your models here.
