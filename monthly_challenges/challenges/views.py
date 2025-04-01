from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("Eat no meat for the entire month!") #This is the response that will be returned when the URL is /challenges/january

def february(request):
    return HttpResponse("Walk for at least 30 minutes every day.") #This is the response that will be returned when the URL is /challenges/february