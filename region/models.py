from django.db import models


# model pour region
class Region(models.Model):
    code_reg = models.CharField(max_length=25)
    nom_reg = models.CharField(max_length=25)