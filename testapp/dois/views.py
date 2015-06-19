# Create your views here.
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic
import reversion

from .models import Dois
from .forms import DoisForm


class DoisCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dois
    form_class = DoisForm
    success_url = reverse_lazy('dois_list')


class DoisUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'dois/dois_form.html'
    model = Dois
    form_class = DoisForm
    success_url = reverse_lazy('dois_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        version_list = reversion.get_unique_for_object(self.object)
        context.update(
            {
                'version_list': version_list
            }
        )
        return context


class DoisListView(generic.ListView):
    model = Dois
