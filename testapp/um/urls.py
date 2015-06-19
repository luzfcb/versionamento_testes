try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from django.conf.urls import url

from .views import UmCreateView, UmListView, UmUpdateView

urlpatterns = [
    url(r'^um/$', UmListView.as_view(), name='um_list'),
    url(r'^um/create/$', UmCreateView.as_view(), name='um_create'),
    url(r'^um/update/(?P<pk>\d+)/$', UmUpdateView.as_view(), name='um_update'),
]
