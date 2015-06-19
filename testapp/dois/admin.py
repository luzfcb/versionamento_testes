from django.contrib import admin
import reversion
from .models import Dois

@admin.register(Dois)
class DoisAdmin(reversion.admin.VersionAdmin):
    list_display = ['texto', 'versao', 'dira']

    def dira(self, object):

        return '{}'.format(dir(object))
    dira.short_description = 'dir'
