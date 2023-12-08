from django.shortcuts import render, HttpResponse


def home(request):
    a = 10/0
    return HttpResponse("home")