from django import forms


from core.forms import SaveHelper

from .models import ImpliUm

class ImpliUmForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImpliUmForm, self).__init__(*args, **kwargs)
        self.helper = SaveHelper(self)

    class Meta:
        model = ImpliUm
        fields = [
            'texto',
            'versao'
        ]
