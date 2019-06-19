from django.shortcuts import render
from .models import Post

def blog(request):
    context = {
}
    return render(request,'blog.html',context)
