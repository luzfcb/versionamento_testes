try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from django.conf.urls import url

from .views import DoisCreateView, DoisListView, DoisUpdateView

urlpatterns = [
    url(r'^dois/$', DoisListView.as_view(), name='dois_list'),
    url(r'^dois/create/$', DoisCreateView.as_view(), name='dois_create'),
    url(r'^dois/update/(?P<pk>\d+)/$', DoisUpdateView.as_view(), name='dois_update'),
]
