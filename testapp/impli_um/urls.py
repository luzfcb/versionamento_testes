try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from django.conf.urls import url

from .views import ImpliUmCreateView, ImpliUmListView, ImpliUmUpdateView

urlpatterns = [
    url(r'^impli_um/$', ImpliUmListView.as_view(), name='impli_um_list'),
    url(r'^impli_um/create/$', ImpliUmCreateView.as_view(), name='impli_um_create'),
    url(r'^impli_um/update/(?P<pk>\d+)/$', ImpliUmUpdateView.as_view(), name='impli_um_update'),
]