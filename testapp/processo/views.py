from braces.views import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import Livro, Pizza
from .forms import LivroForm, PizzaForm

from auditavel.views import AuditavelViewMixin


class LivroCreateView(LoginRequiredMixin, generic.CreateView, AuditavelViewMixin):
    model = Livro
    form_class = LivroForm


class LivroUpdateView(LoginRequiredMixin, generic.UpdateView, AuditavelViewMixin):
    model = Livro
    form_class = LivroForm


class LivroListView(generic.ListView):
    model = Livro





class PizzaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Pizza
    form_class = PizzaForm


class PizzaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Pizza
    form_class = PizzaForm


class PizzaListView(generic.ListView):
    model = Pizza
