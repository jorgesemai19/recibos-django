from django.conf.urls import url
from .import views

app_name = 'menu_lista'

urlpatterns  = [
    url(r'^$',views.menu_lista, name = 'menu'),
]
