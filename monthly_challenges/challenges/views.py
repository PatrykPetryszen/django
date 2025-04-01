from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    if month == "august":
        return HttpResponse("It's your birthday!")
    return HttpResponse("The month is " + month) #This is the response that will be returned when the URL is /challenges/<month>