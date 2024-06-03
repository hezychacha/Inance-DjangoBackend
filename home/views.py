from django.shortcuts import render,HttpResponse
from . models import services
from django.http import JsonResponse

# Create your views here.

def index(request):
    service = services.objects.all()[:3]
    return render(request,'index.html',{'service':service})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def service(request):
     service = services.objects.all()[:3]
     return render(request,'service.html',{'service':service})

def viewMore(request):
    service = list(services.objects.all().values())
    return JsonResponse({'services':service})


# def service(request):
#     return render(request,'service.html')

