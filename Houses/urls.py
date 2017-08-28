from django.conf.urls import url
from . import views
from Houses.views import ConfirmationView

urlpatterns = [
    url(r'^$', views.house_index, name='index'),
    url(r'^house/(?P<house_id>[0-9]+)$', views.house, name='house'),
    url(r'^confirmation$', ConfirmationView.as_view(), name="confirmation"),
]