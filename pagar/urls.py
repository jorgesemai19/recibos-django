from django.conf.urls import url
from .import views
import reportlab

app_name = 'pagos'

urlpatterns  = [
    url(r'^$',views.pagar, name = 'pagar'),

    url(r'^mostrar/$',views.mostrar, name='mostrar'),
    #url(r'^generar_pdf/$',views.pdfvista, name='pdf'),

]
