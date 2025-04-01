from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("Eat no meat for the entire month!") #This is the response that will be returned when the URL is /challenges/january

def february(request):
    return HttpResponse("Walk for at least 30 minutes every day.") #This is the response that will be returned when the URL is /challenges/february

def monthly_challenge(request, month):
    if month == "august":
        return HttpResponse("It's your birthday!")
    return HttpResponse("The month is " + month) #This is the response that will be returned when the URL is /challenges/<month>