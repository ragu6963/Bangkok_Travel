from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    return render(request, "accounts/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("posts:home")
        else:

            return render(
                request,
                "signin.html",
                {"error": "username or password is incorrect."},
            )
    else:
        return render(request, "accounts/signin.html")
