from django.urls import path, include
from .views import helloapi, missingPeople, safeSpotData

urlpatterns = [
    path("hello/", helloapi),
    path("missingPeople/<int:page>", missingPeople),
    path("safeSpot/<int:pageIndex>", safeSpotData)
]
