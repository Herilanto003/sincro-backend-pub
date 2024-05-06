from django.db import models
from utilisateurs.models import Membre


# model pour rapport
class Rapport(models.Model):
    code_rap = models.CharField(max_length=25, unique=True)
    titre = models.CharField(max_length=25)
    description = models.TextField()
    date = models.DateField()
    membre = models.ForeignKey(
        Membre,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )