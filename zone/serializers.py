from rest_framework import serializers
from .models import Zone


class ZoneSerializer(serializers.ModelSerializer):
    code_zone = serializers.CharField(read_only=True)

    class Meta:
        model = Zone
        fields = '__all__'


    def save(self, **kwargs):
        zone = super().save(**kwargs)  
        zone.code_zone = "ZONE-" + str(zone.id).zfill(3)
        zone.save()  
        return zone