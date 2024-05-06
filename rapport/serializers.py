from rest_framework import serializers
from .models import Rapport


class RapportSerializer(serializers.ModelSerializer):
    code_rap = serializers.CharField(read_only=True)

    class Meta:
        model = Rapport
        fields = '__all__'


    def save(self, **kwargs):
        rapport = super().save(**kwargs)  
        rapport.code_rap = "RPR-" + str(rapport.id).zfill(3)
        rapport.save()  
        return rapport