from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from registro.forms import listado
from registro.models import personal,lista_registro,dependencia,concepto,pago,recibo
from datetime import datetime, date, time
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A2,A4,A5,A6, landscape
import locale
import os
from django.db.models import Count, Value, F



# Create your views here.

@login_required(login_url="/login/")
def pagar(request):
    return render(request,'pagar/pagos.html')

@login_required(login_url="/login/")
def mostrar(request):
    hoy = datetime.now() #fecha actual
    dia = hoy.strftime("%d") # fecha con formato
    obtener_mes = date.today().month
    meses  = {1:"enero", 2:"febrero", 3:"marzo", 4:"abril", 5:"mayo", 6:"junio", 7:"julio", 8:"agosto", 9:"setiembre", 10:"octubre", 11:"noviembre", 12:"diciembre"}
    mes = str(meses[obtener_mes])
    year = hoy.strftime("%Y")
    if request.method == 'POST':
        cedu = request.POST.get('ced')
        if not cedu :
            return redirect('http://127.0.0.1:8000/pagar/')
        else:
            p = personal.objects.filter(cedula = cedu)
            if not p:
                return redirect('http://127.0.0.1:8000/pagar/')
            else:
                iden = int(p[0].id)
                li = lista_registro.objects.filter(personal_id = iden, pago_id = 2)
                adicion = 0
                contador=0
                for k in li:
                    adicion += int(k.monto)
                    contador += 1
    ###Datos para rellenar el recibo###
    nombre = str(p[0].nombre)+ " " +str(p[0].apellido)
    cedula =  int(p[0].cedula)
    str1 = format(adicion, ',d')
    str2 = format(cedula, ',d')
    print(contador)

    #de pagado 'no' a pagado 'si'
    pagobj = pago.objects.get(pagado='si')
    for indice in range(0,contador):
        listobj = lista_registro.objects.filter(personal_id = iden, pago_id = 2).first()
        if listobj:
            listobj.pago_id= pagobj
            listobj.save()
    obj = recibo(
        dia = dia,
        mes = mes,
        year = year,
    )
    obj.save()

    obj2 = recibo.objects.order_by('-id')
    iden2 = str(obj2[0].id)
    print(iden2)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename=hello.pdf'
    # Se crea el objeto PDF, usando el objeto de respuesta como si fuese un "archivo".
    #Dibujo de el RECIBO
    p = canvas.Canvas(response,pagesize = landscape(A5))
    p.line(20,20,20,400)
    p.line(20,20,575,20)
    p.line(575,400,575,20)
    p.line(20,400,575,400)
    p.line(133,315,153,315)
    p.line(170,315,250,315)
    p.line(268,315,310,315)
    p.line(155,290,230,290)
    p.setFont('Times-Roman',20)

    p.drawString(205, 380,"RECIBO DE DINERO")
    p.setFont('Times-Roman',15)
    p.drawString(260,365,"(Uso Interno)")
    p.drawString(70, 315,"Asunción,")
    p.drawString(135, 317,dia)
    p.drawString(155,315,"de")
    p.drawString(175,317,mes)
    p.drawString(253,315,"de")
    p.drawString(270,317,year)
    p.drawString(70,290,"Recibimos de ")
    p.drawString(160,293,"MVA S.A.")
    p.drawString(182,265,"Guaraníes")
    p.drawString(110,270, str1)
    p.line(70,265,180,265)
    p.drawString(70,240,"En concepto de: ")
    p.drawImage("pagar/mva.png", 40, 327, width=100, height=70)
    a=220
    for j in li:
        cadena = "* "+ str(j.concepto_id)+" de "+str(j.fecha_realizado)
        p.drawString(70,a,cadena)
        a=a-20
    #id =
    p.line(360,150,500,150)
    p.drawString(410,135,"Firma")
    p.line(320,100,560,100)
    p.drawString(365,80,"Aclaración de firma")
    p.drawString(330,105,nombre)
    p.line(360,50,500,50)
    p.drawString(410,30,"C.I.Nro.")
    p.drawString(410,55,str2)
    p.drawString(430, 380,"NRO: ")
    p.drawString(470,380, iden2)

    # Se cierra el objeto PDF, y terminamos.
    p.showPage()
    p.save()
    os.system("hello.pdf")

    return response
"""
def previsualizar(request):
    hoy = datetime.now() #fecha actual
    dia = hoy.strftime("%d") # fecha con formato
    obtener_mes = date.today().month
    meses  = {1:"enero", 2:"febrero", 3:"marzo", 4:"abril", 5:"mayo", 6:"junio", 7:"julio", 8:"agosto", 9:"setiembre", 10:"octubre", 11:"noviembre", 12:"diciembre"}
    mes = str(meses[obtener_mes])
    year = hoy.strftime("%Y")
    if request.method == 'POST':
        cedu = request.POST.get('ced')
        if not cedu :
            return redirect('http://127.0.0.1:8000/pagar/')
        else:
            p = personal.objects.filter(cedula = cedu)
            if not p:
                return redirect('http://127.0.0.1:8000/pagar/')
            else:
                iden = int(p[0].id)
                li = lista_registro.objects.filter(personal_id = iden, pago_id = 2)
                adicion = 0
                contador=0
                for k in li:
                    adicion += int(k.monto)
                    contador += 1
"""
