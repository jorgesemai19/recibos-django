from django.conf.urls import url
from .import views

app_name = 'busqueda'

urlpatterns  = [
    url(r'^$',views.pedircedula, name = 'pedir'),
    url(r'^muestra/$',views.buscar, name = 'buscar'),
]
