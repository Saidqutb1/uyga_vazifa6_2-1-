from django.urls import path
from .views import sayhu

urlpatterns = [
    path('', sayhu)
]