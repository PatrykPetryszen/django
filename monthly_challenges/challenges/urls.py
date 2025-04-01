from django.urls import path
from . import views #This imports the views.py file in the same directory together with function index there

urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number), #This will call the monthly_challenge_by_number function in views.py and pass the month as an integer argument
    path("<str:month>", views.monthly_challenge), #This will call the monthly_challenge function in views.py and pass the month as an string argument, but /notmonth will also be in use
]