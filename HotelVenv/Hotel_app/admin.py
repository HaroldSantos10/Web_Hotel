from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(tblpais)
admin.site.register(tblciudad)
admin.site.register(tblhotel)
admin.site.register(tbltemporada)
admin.site.register(tbltipo_habitacion)
admin.site.register(tblhabitacion)
admin.site.register(tblcliente)
admin.site.register(tblprecio_habitacion)
admin.site.register(tblreservacion)

admin.site.register(tblservicio)
admin.site.register(tbltipo_pago)
admin.site.register(tblpago)
admin.site.register(tblsuscripciones)