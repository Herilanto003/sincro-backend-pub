from django.urls import path
from .views import DetailDistrict, ListeCreerDistrict


urlpatterns = [
    path('api/', ListeCreerDistrict.as_view()),
    path('api/<int:pk>', DetailDistrict.as_view())
] 
