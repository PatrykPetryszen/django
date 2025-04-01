from django.urls import path
from . import views #This imports the views.py file in the same directory together with function index there

urlpatterns = [
    path("january", views.index) #If the URL is /january, call the index function in views.py
]