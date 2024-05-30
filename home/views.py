from django.shortcuts import render,HttpResponse
from . models import services

# Create your views here.

def index(request):
    service = services.objects.all()
    return render(request,'index.html',{'service':service})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')