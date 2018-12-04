from django.conf.urls import url
from .import views

app_name = 'ingresar'

urlpatterns  = [
    url(r'^$',views.login_vista, name = 'login'),
    url(r'^logout/$',views.logout_vista, name = 'logout')
]
