from django import forms


from core.forms import SaveHelper

from .models import Um

class UmForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UmForm, self).__init__(*args, **kwargs)
        self.helper = SaveHelper(self)

    class Meta:
        model = Um
        fields = [
            'texto',
            'versao'
        ]
