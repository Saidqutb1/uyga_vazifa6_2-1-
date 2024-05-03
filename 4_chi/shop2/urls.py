from django.urls import path
from .views import *

urlpatterns = [
    path('shop2/', get_info)
]