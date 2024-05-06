from rest_framework import generics
from .serializers import RapportSerializer
from .models import Rapport


class ListeCreerRapport(generics.ListCreateAPIView):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer


class DetailRapport(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer
