from django.db import models
from region.models import Region


# models pour district
class District(models.Model):
    code_dist = models.CharField(max_length=25)
    nom_dist = models.CharField(max_length=25)
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )
