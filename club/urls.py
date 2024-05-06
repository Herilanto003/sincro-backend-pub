from django.urls import path
from .views import DetailClub, ListeCreerClub


urlpatterns = [
    path('api/', ListeCreerClub.as_view()),
    path('api/<int:pk>', DetailClub.as_view())
] 
