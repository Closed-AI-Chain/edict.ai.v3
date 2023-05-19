from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('generatevideo/', views.generateVideo,name="generatevideo"),
    path('video/', views.showVideo,name="generatevideo"),
    path('', views.index,name="index"),
    path('test', views.test,name="test"),
    path('register/', views.register,name="register"),
    path('form/', views.form,name="form"),
    
    
    
]
