from django.urls import path
from .views import DetailMembre, ListeCreerMembre


urlpatterns = [
    path('api/', ListeCreerMembre.as_view()),
    path('api/<int:pk>', DetailMembre.as_view())
] 
