from django.shortcuts import render,redirect
from registro.models import lista_registro, personal
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def pedircedula(request):
    return render(request,'buscar/pedirced.html')

@login_required(login_url="/login/")
def buscar(request):
    if request.method == 'POST':
        cedu = request.POST.get('ced')
        if not cedu:
            return redirect('http://127.0.0.1:8000/buscar/')
        else:
            p = personal.objects.filter(cedula = cedu)
            if not p:
                return redirect('http://127.0.0.1:8000/buscar/')
            else:
                iden = int(p[0].id)
                li1 = lista_registro.objects.filter(personal_id = iden, pago_id = 2)
                li2 = lista_registro.objects.filter(personal_id = iden, pago_id = 1)
                adicion = 0
                for k in li1:
                    adicion += int(k.monto)
                context = {
                'li1':li1,
                'li2':li2,
                'p':p,
                'adicion':adicion,
                }
    return render(request,'buscar/buscar.html',context)
