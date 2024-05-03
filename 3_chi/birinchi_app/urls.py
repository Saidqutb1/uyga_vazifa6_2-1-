from django.urls import path
from .views import *

urlpatterns = [
    path('1_chi/', get_info)
]