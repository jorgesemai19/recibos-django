from django.shortcuts import render,redirect
from registro.models import lista_registro
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def pagos_pendientes(request):
    lista = lista_registro.objects.filter(pago_id = '2')
    suma = 0

    for k in lista:
        suma += int(k.monto) 

    context = {
    'lista':lista,
    'suma':suma,
    }
    return render(request,'pagos_pendientes/pendientes.html',context)
