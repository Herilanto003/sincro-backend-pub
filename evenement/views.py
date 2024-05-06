from rest_framework import generics
from .serializers import EvenementSerializer
from .models import Evenement


class ListeCreerEvenement(generics.ListCreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer


class DetailEvenement(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
