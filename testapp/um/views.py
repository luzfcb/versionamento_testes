# Create your views here.
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .models import Um
from .forms import UmForm

class UmCreateView(LoginRequiredMixin, generic.CreateView):
    model = Um
    form_class = UmForm
    success_url = reverse_lazy('um_list')


class UmUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Um
    form_class = UmForm
    success_url = reverse_lazy('um_list')


class UmListView(generic.ListView):
    model = Um
