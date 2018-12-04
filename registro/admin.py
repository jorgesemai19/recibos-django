from django.contrib import admin
from .models import dependencia, concepto, personal, pago, lista_registro,recibo


admin.site.register(dependencia)
admin.site.register(concepto)
admin.site.register(personal)
admin.site.register(lista_registro)
admin.site.register(pago)
admin.site.register(recibo)
