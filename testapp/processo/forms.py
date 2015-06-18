from django.forms import ModelForm

from .models import Livro, Pizza

from core.forms import SaveHelper


class LivroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LivroForm, self).__init__(*args, **kwargs)
        self.helper = SaveHelper(self)

    class Meta:
        model = Livro
        fields = ['nome', 'autor']


class PizzaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PizzaForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = SaveHelper(self)

    class Meta:
        model = Pizza
        fields = ['nome', 'sabor']
