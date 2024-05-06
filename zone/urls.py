from django.urls import path
from .views import DetailZone, ListeCreerZone


urlpatterns = [
    path('api/', ListeCreerZone.as_view()),
    path('api/<int:pk>', DetailZone.as_view())
]
