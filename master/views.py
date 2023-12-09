from django.shortcuts import render, HttpResponse
from master import signals_1

# def home(request):
#     a = 10/0
#     return HttpResponse("home")

def home(request):
    signals_1.notification.send(sender=None, request=request, user=["Ujjwal", "gunjan"], abc=['hariom'])
    return HttpResponse("This is homePage!")