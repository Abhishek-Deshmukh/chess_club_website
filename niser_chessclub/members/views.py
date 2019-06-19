from django.shortcuts import render
from .models import Member

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def members(request):
    context = {
            'members':Member.objects.all(),
    }
    return render(request,'members.html',context)

def contact(request):
    return render(request,'contact.html')
