from django.db import models



class dependencia(models.Model):
    nombre_dependencia = models.CharField(max_length=100)
    def __str__(self):
	       return self.nombre_dependencia


class concepto(models.Model):
    concepto_def = models.CharField(max_length=100)
    def __str__(self):
	       return self.concepto_def

class personal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    def __str__(self):
	       return self.nombre + " " + self.apellido + " - " + self.cedula + " - " + str(self.id)

class pago(models.Model):
    pagado = models.CharField(max_length=10)
    def __str__(self):
        return self.pagado


class lista_registro(models.Model):
    personal_id = models.ForeignKey(personal, on_delete=models.CASCADE)
    dependencia_id = models.ForeignKey(dependencia, on_delete=models.CASCADE)
    concepto_id = models.ForeignKey(concepto, on_delete=models.CASCADE)
    fecha_realizado = models.DateField(null=True,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=1000)
    pago_id = models.ForeignKey(pago, on_delete=models.CASCADE, default=2)
    monto = models.CharField(max_length=100)
    def __str__(self):
	       return "===> " + self.descripcion + " <==="

class recibo(models.Model):
    dia = models.IntegerField(null=True, blank=True)
    mes = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.dia)+ "-" +self.mes+ "-" +str(self.year)
