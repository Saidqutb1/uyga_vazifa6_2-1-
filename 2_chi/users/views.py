from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saybye(request):
    return HttpResponse('Goodbye')