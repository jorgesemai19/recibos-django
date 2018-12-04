from django.conf.urls import url
from .import views

app_name = 'suma_diaria'

urlpatterns  = [
    url(r'^$',views.suma, name = 'suma'),
]
