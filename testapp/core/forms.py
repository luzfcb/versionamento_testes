from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

# place form definition here
class SaveHelper(FormHelper):
    def __init__(self, form=None):
        super().__init__(form)
        self.layout.append(Submit(name='save', value='Salvar'))
        self.form_show_errors = True
        self.render_required_fields = True
