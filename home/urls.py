from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('contact', views.contact,name='contact'),
    path('about', views.about,name='about'),
    path('service', views.service,name='service'),
    path('viewmore', views.viewMore,name='viewmore'),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    path('logout', views.logout,name='logout'),
]