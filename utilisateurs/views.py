from rest_framework import generics
from .serializers import MembreSerializer
from .models import Membre


class ListeCreerMembre(generics.ListCreateAPIView):
    queryset = Membre.objects.all()
    serializer_class = MembreSerializer


class DetailMembre(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membre.objects.all()
    serializer_class = MembreSerializer
