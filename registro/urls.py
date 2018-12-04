from django.conf.urls import url
from .import views

app_name = 'regis'

urlpatterns  = [
    url(r'^$',views.lista_registros, name='lista_registros'),

    url(r'^autocompletar/$', views.autocompletar, name='autocompletar'),

    url(r'^guardar/$', views.guardar, name='guardar'),
]
