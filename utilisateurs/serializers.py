from rest_framework import serializers
from .models import Membre


class MembreSerializer(serializers.ModelSerializer):
    code_membre = serializers.CharField(read_only=True)
    compte = serializers.CharField(read_only=True)
    titre = serializers.CharField(read_only=True)

    class Meta:
        model = Membre
        fields = '__all__'


    def save(self, **kwargs):
        club = super().save(**kwargs)  
        club.code_membre = "MBR-" + str(club.id).zfill(3)
        club.save()  
        return club