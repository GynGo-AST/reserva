from django.contrib import admin
from pedidos.models import Aula, Recurso, Profesor, Reserva

# Register your models here.
admin.site.register(Aula)
admin.site.register(Recurso)
admin.site.register(Profesor)
admin.site.register(Reserva)