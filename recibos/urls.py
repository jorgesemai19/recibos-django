from django.conf.urls import url,include
from django.contrib import admin

urlpatterns  = [
    url(r'^admin/',admin.site.urls),
    url(r'^login/',include('login.urls')),
    url(r'^registro/',include('registro.urls')),
    url(r'^menu/',include('menu.urls')),
    url(r'^pagar/',include('pagar.urls')),
    url(r'^suma_diaria/',include('suma_diaria.urls')),
    url(r'^pagos_pendientes/',include('pagos_pendientes.urls')),
    url(r'^buscar/',include('buscar.urls')),
]
