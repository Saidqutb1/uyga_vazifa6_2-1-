from django.urls import path
from .views import *

urlpatterns = [
    path('places', get_info)
]