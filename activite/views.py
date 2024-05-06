from rest_framework import generics
from .serializers import ActiviteSerializer
from .models import Activite


class ListeCreerActivite(generics.ListCreateAPIView):
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer


class DetailActivite(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer
