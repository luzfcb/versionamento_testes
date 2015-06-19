from django.db import models
import reversion



class Dois(models.Model):
    texto = models.TextField(blank=False)
    versao = models.PositiveIntegerField(default=1)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # if self.id:
        #     anterior = Dois.objects.get(id=self.id)
        #     self.versao = anterior.versao + 1
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Varios "DOIS"'


reversion.register(Dois)
