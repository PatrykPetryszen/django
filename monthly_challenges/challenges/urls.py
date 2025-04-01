from django.urls import path
from . import views #This imports the views.py file in the same directory together with function index there

urlpatterns = [
    path("january", views.january), #If the URL is /january, call the index function in views.py
    path("february", views.february),
    path("<month>", views.monthly_challenge), #This will call the monthly_challenge function in views.py and pass the month as an argument
]