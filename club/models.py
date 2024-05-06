from django.db import models
from zone.models import Zone


# models pour clubs
class Club(models.Model):
    code_club = models.CharField(max_length=25)
    nom_club = models.CharField(max_length=25)
    zone = models.ForeignKey(
        Zone,
        on_delete=models.CASCADE
    )
