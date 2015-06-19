from django import forms


from core.forms import SaveHelper

from .models import Dois

class DoisForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DoisForm, self).__init__(*args, **kwargs)
        self.helper = SaveHelper(self)

    class Meta:
        model = Dois
        fields = [
            'texto',
            'versao'
        ]
