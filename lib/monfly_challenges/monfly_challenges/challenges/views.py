from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    'december': None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {
        'months': months
    })


def monfly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    else:
        redirect_month = months[month - 1]
        redirect_path = reverse('month-challenge', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)


def monfly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'title': f'{month} challenge',
            'month': f'{month}\'s challenge',
            'text': challenge_text,
        })
    except:
        return HttpResponseNotFound("Where is month???")
