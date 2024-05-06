from django.urls import path
from .views import DetailActivite, ListeCreerActivite


urlpatterns = [
    path('api/', ListeCreerActivite.as_view()),
    path('api/<int:pk>', DetailActivite.as_view())
]
