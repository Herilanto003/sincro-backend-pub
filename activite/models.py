from django.db import models
from evenement.models import Evenement


# model pour activites
class Activite(models.Model):
    code_act = models.CharField(max_length=25, unique=True)
    titre = models.CharField(max_length=25)
    description = models.TextField()
    date = models.DateField()
    dure = models.IntegerField()
    evenement = models.ForeignKey(
        Evenement,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )