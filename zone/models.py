from django.db import models
from district.models import District


# models pour zone
class Zone(models.Model):
    code_zone = models.CharField(max_length=25)
    nom_zone = models.CharField(max_length=25)
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE
    )
