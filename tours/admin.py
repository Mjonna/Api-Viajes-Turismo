from django.contrib import admin

from .models import Destino, Guia, Tour, Cliente, Reserva

admin.site.register(Destino)
admin.site.register(Guia)
admin.site.register(Tour)
admin.site.register(Cliente)
admin.site.register(Reserva)
