from rest_framework import generics
from .serializers import ClubSerializer
from .models import Club


class ListeCreerClub(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class DetailClub(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
