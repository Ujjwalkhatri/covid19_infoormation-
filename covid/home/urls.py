from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name = 'home'),
    path("about",views.about, name = 'about'),
    path("symptoms",views.symptoms, name = 'symptoms'),
    path("protection",views.protection, name= 'protection'),
    path("effect",views.effect, name = 'effect'),
   
]
