from django.urls import path
from .views import *

urlpatterns = [
    path('', get_info, name='get_info')
]