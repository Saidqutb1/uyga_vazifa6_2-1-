from django.urls import path
from .views import *

urlpatterns = [
    path('biznes/', get_info)
]