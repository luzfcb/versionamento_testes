from django.db import models

# Create your models here.
from versionfield import VersionField


class ImpliUm(models.Model):
    texto = models.TextField(blank=False)
    versao = VersionField()
