from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:month>", views.monfly_challenge_by_number),
    path("<str:month>", views.monfly_challenge, name='month-challenge'),
]
