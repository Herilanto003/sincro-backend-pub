from rest_framework import serializers
from .models import Club


class ClubSerializer(serializers.ModelSerializer):
    code_club = serializers.CharField(read_only=True)

    class Meta:
        model = Club
        fields = '__all__'


    def save(self, **kwargs):
        club = super().save(**kwargs)  
        club.code_club = "CLUB-" + str(club.id).zfill(3)
        club.save()  
        return club