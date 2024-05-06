from django.urls import path
from .views import DetailRegion, ListeCreerRegion


urlpatterns = [
    path('api/', ListeCreerRegion.as_view()),
    path('api/<int:pk>', DetailRegion.as_view())
]
