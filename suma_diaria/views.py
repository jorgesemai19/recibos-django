from django.shortcuts import render,redirect
from registro.models import lista_registro
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required(login_url="/login/")
def suma(request):
    today = datetime.now() #fecha actual
    dateFormat = today.strftime("%Y-%m-%d") # fecha con formato
    lista = lista_registro.objects.filter(fecha_registro = dateFormat)
    adicion = 0
    for k in lista:
        adicion += int(k.monto)

    sumatotal = format(adicion, ',d')
    context = {
    'lista':lista,
    'adicion':adicion,
    'sumatotal':sumatotal
    }
    return render(request,'suma_diaria/suma.html',context)
