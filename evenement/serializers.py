from rest_framework import serializers
from .models import Evenement


class EvenementSerializer(serializers.ModelSerializer):
    code_ev = serializers.CharField(read_only=True)

    class Meta:
        model = Evenement
        fields = '__all__'


    def save(self, **kwargs):
        evenement = super().save(**kwargs)  
        evenement.code_ev = "EVNM-" + str(evenement.id).zfill(3)
        evenement.save()  
        return evenement