from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_info(request):
    return HttpResponse('World is not small')