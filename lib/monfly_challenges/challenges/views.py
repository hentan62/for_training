from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    'january': 'first challenge',
    'february': 'second challenge',
    'march': 'third challenge',
    'april': 'fourth  challenge',
    'may': 'fifth challenge',
    'june': 'sixth challenge',
    'july': 'seventh challenge',
    'august': 'eighth challenge',
    'september': 'ninth challenge',
    'october': 'tenth challenge',
    'november': 'eleventh challenge',
    'december': 'twelfth challenge'
}


def monfly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    else:
        redirect_month = months[month - 1]
        return HttpResponseRedirect(redirect_month)


def monfly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Where is month???")
