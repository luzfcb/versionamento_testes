from django.conf import settings
from django.db import models

# Create your models here.
class AuditavelAbstractModel(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='criado_por')

    modificado_em = models.DateTimeField(auto_now=True)
    modificado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='modificado_por')

    class Meta:
        abstract = True
