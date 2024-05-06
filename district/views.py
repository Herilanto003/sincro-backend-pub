from rest_framework import generics
from .serializers import DistrictSerializer
from .models import District


class ListeCreerDistrict(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class DetailDistrict(generics.RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
