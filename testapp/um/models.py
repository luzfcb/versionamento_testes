from django.db import models

# Create your models here.
from versionfield import VersionField


class Um(models.Model):
    texto = models.TextField(blank=False)
    versao = models.PositiveIntegerField(default=1)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.id:
            anterior = Um.objects.get(id=self.id)
            self.versao = anterior.versao + 1
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{}-{}'
