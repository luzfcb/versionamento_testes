# Create your views here.
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .models import ImpliUm
from .forms import ImpliUmForm

class ImpliUmCreateView(LoginRequiredMixin, generic.CreateView):
    model = ImpliUm
    form_class = ImpliUmForm
    success_url = reverse_lazy('impli_um_list')


class ImpliUmUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = ImpliUm
    form_class = ImpliUmForm
    success_url = reverse_lazy('impli_um_list')


class ImpliUmListView(generic.ListView):
    model = ImpliUm
