from django.conf.urls import url

from .views import LivroCreateView, LivroUpdateView, LivroListView, PizzaCreateView, PizzaListView, PizzaUpdateView

urlpatterns = [
    url(r'^livro/$', LivroListView.as_view(), name='livro_list'),
    url(r'^livro/create/$', LivroCreateView.as_view(), name='livro_create'),
    url(r'^livro/update/(?P<pk>\d+)/$', LivroUpdateView.as_view(), name='livro_update'),

    url(r'^pizza/$', PizzaListView.as_view(), name='pizza_list'),
    url(r'^pizza/create/$', PizzaCreateView.as_view(), name='pizza_create'),
    url(r'^pizza/update/(?P<pk>\d+)/$', PizzaUpdateView.as_view(), name='pizza_update'),
]
