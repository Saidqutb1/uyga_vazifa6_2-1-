from django.urls import path
from .views import *

urlpatterns = [
    path('shop1/', get_info, name='get_info')
]