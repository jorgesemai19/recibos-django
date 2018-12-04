from django.shortcuts import render
from .models import personal,lista_registro,dependencia,concepto
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import comparar_cedula,listado
from datetime import datetime

@login_required(login_url="/login/")
def lista_registros(request):
    form  = comparar_cedula(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request,'registro/reg.html',context)

def autocompletar(request):
    form_auto = comparar_cedula(request.POST or None)
    if form_auto.is_valid():
        datos = form_auto.cleaned_data
        ci = datos.get("cedula")
        print (ci)
        nombres2 = personal.objects.filter(cedula = ci)
        depen = dependencia.objects.all()
        concep = concepto.objects.all()
        lista2 = lista_registro.objects.all()

    context2 = {
    'nombres2':nombres2,
    'lista2':lista2,
    'depen':depen,
    'concep':concep,
    }
    return render(request, 'registro/guardar.html',context2)

def guardar(request):
    if request.method == "POST":
        idpersona = int(request.POST.get('id'))
        persona = personal.objects.get(id=idpersona)
        idep = int(request.POST.get('dependencia'))
        dep = dependencia.objects.get(id=idep)
        idcon = int(request.POST.get('concepto'))
        con = concepto.objects.get(id=idcon)
        fecha = request.POST.get('fecha')
        db_registro = lista_registro(
            personal_id=persona,
            fecha_realizado=fecha,
            dependencia_id=dep,
            concepto_id=con,
            descripcion=request.POST.get('descripcion'),
            monto=request.POST.get('monto'),
        )
        db_registro.save()

    return render(request, 'registro/exito.html')
