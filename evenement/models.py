from django.db import models
from utilisateurs.models import Membre


# model pour evenements
class Evenement(models.Model):
    code_ev = models.CharField(max_length=25, unique=True)
    titre = models.CharField(max_length=25)
    description = models.TextField()
    date = models.DateField()
    dure = models.IntegerField()
    membre = models.ForeignKey(
        Membre,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )