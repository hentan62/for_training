from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


monthly_cha

def monfly_challenge_by_number(request, month):
    return HttpResponse(month)

def monfly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = 'hello world!'
    elif month == "february":
        challenge_text = 'This is February'
    else:
        return HttpResponseNotFound("Месяц не найден")
    return  HttpResponse(challenge_text)
