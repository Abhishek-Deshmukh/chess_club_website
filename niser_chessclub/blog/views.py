from django.shortcuts import render
from .models import Post

def blog(request):
    context = {
            'posts' : Post.objects.all()
}
    return render(request,'blog.html',context)
