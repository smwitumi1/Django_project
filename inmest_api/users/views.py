from django.shortcuts import render

from django.http import HttpResponse

def User(request):
    return HttpResponse("user")
