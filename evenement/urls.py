from django.urls import path
from .views import DetailEvenement, ListeCreerEvenement


urlpatterns = [
    path('api/', ListeCreerEvenement.as_view()),
    path('api/<int:pk>', DetailEvenement.as_view())
]
