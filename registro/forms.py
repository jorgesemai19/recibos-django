from django import forms
from. import models
from . models import personal, lista_registro

class comparar_cedula(forms.ModelForm):
    class  Meta:
        model = models.personal
        fields = ['cedula']
        exclude = ['nombre', 'apellido']

class listado(forms.ModelForm):
    class Meta:
        model = models.lista_registro
        fields =['fecha_realizado','monto','descripcion','personal_id', 'pago_id', 'dependencia_id','concepto_id'] 
        exclude = []
