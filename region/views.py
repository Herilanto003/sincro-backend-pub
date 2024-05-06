from rest_framework import generics
from .serializers import RegionSerializer
from .models import Region


class ListeCreerRegion(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DetailRegion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
