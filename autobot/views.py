from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import logging

from social_django.models import UserSocialAuth
from .models import Greeting

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    try:
        token = UserSocialAuth.objects.get(user=request.user).access_token
    except Exception:
        token = 'unknown'

    return render(request, "index.html", {'token': token})

@login_required
def login(request):
    return render(request, "index.htm")

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
