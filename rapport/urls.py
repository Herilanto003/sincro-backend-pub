from django.urls import path
from .views import DetailRapport, ListeCreerRapport


urlpatterns = [
    path('api/', ListeCreerRapport.as_view()),
    path('api/<int:pk>', DetailRapport.as_view())
]
