from django.shortcuts import render
from django.conf import settings

def home(request):
    MAPS_API_KEY = settings.MAPS_API_KEY
    context={
        "MAPS_API_KEY":MAPS_API_KEY
    }

    return render(request, "posts/home.html",context)
