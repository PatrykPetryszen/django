from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Get fit",
    "february": "Get a job",
    "march": "Get a girlfriend",
    "april": "Get a car",
    "may": "Get a house",
    "june": "Get a life",
    "july": "Get a dog",
    "august": "Your birhday",
    "september": "Eat no meat",
    "october": "Learn Django",
    "november": "Walk for at least 20 minutes",
    "december": "Learn Django"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        text_to_month = monthly_challenges[month]
        return HttpResponse(text_to_month)
    except KeyError:
        return HttpResponseNotFound("Please provide the name of the month")