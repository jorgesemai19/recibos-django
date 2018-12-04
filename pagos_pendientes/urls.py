from django.conf.urls import url
from .import views

app_name = 'pendientes'

urlpatterns  = [
    url(r'^$',views.pagos_pendientes, name = 'pagos_pendientes'),
]
