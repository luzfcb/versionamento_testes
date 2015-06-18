from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
import reversion
from simple_history.models import HistoricalRecords

from auditavel.models import AuditavelAbstractModel

@python_2_unicode_compatible
class Pessoa(models.Model):
    texto = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.texto if self.texto else '')

    class Meta:
        app_label = 'processo'

reversion.register(Pessoa)



class Pizza(models.Model):
    nome = models.CharField(max_length=128)
    sabor = models.CharField(max_length=128)
    # criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='criado_por')
    modificado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')

    historico = HistoricalRecords()

    @property
    def _history_user(self):
        return self.modificado_por

    @_history_user.setter
    def _history_user(self, value):
        self.modificado_por = value

    @staticmethod
    def get_absolute_url():
        return reverse('pizza_list')

    class Meta:
        app_label = 'processo'




class Livro(AuditavelAbstractModel):
    nome = models.CharField(max_length=128)
    autor = models.CharField(max_length=128)

    historico = HistoricalRecords()

    @staticmethod
    def get_absolute_url():
        return reverse('livro_list')

    class Meta:
        app_label = 'processo'
