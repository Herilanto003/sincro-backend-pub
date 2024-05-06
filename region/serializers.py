from rest_framework import serializers
from .models import Region


class RegionSerializer(serializers.ModelSerializer):
    code_reg = serializers.CharField(read_only=True)

    class Meta:
        model = Region
        fields = ['nom_reg', 'code_reg']


    def save(self, **kwargs):
        region = super().save(**kwargs)  
        region.code_reg = "REG-" + str(region.id).zfill(3)
        region.save()  
        return region