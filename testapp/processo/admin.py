from django.contrib import admin

# Register your models here.
from reversion_compare.admin import CompareVersionAdmin

from .models import Pessoa, Livro


@admin.register(Pessoa)
class PessoaModelAdmin(CompareVersionAdmin):
    pass

@admin.register(Livro)
class LivroModelAdmin(CompareVersionAdmin):
    pass
