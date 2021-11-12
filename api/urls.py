from django.urls import path, include
from .views import helloapi


urlpatterns = [
    path("hello/", helloapi),
]
