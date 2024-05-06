from rest_framework import serializers
from .models import District


class DistrictSerializer(serializers.ModelSerializer):
    code_dist = serializers.CharField(read_only=True)

    class Meta:
        model = District
        fields = '__all__'


    def save(self, **kwargs):
        dist = super().save(**kwargs)  
        dist.code_dist = "DIST-" + str(dist.id).zfill(3)
        dist.save()  
        return dist