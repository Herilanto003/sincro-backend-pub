from rest_framework import serializers
from .models import Activite


class ActiviteSerializer(serializers.ModelSerializer):
    code_act = serializers.CharField(read_only=True)

    class Meta:
        model = Activite
        fields = '__all__'


    def save(self, **kwargs):
        activite = super().save(**kwargs)  
        activite.code_act = "ACT-" + str(activite.id).zfill(3)
        activite.save()  
        return activite