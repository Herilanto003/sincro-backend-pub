from rest_framework import generics
from .serializers import ZoneSerializer
from .models import Zone


class ListeCreerZone(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


class DetailZone(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
