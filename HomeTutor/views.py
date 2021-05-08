from django.shortcuts import render


def home(request):
    """views the home page"""
    return render(request, "home.html", {
    })