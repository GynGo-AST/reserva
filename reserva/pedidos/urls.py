from django.contrib import admin
from django.urls import path
from .views import AulaView, RecursoView, ProfesorView, ReservaView
urlpatterns = [
    path('aula/', AulaView.as_view(), name='aula_list'),
    path('aula/<int:id>', AulaView.as_view(), name='aula_proceso'),
    path('recurso/', RecursoView.as_view(), name='recruso_list'),
    path('recurso/<int:id>', RecursoView.as_view(), name='recurso_proceso'),
    path('profesor/', ProfesorView.as_view(), name='profesor_list'),
    path('profesor/<int:id>', ProfesorView.as_view(), name='profesor_proceso'),
    path('reserva/', ReservaView.as_view(), name='reserva_list'),
    path('reserva/<int:id>', ReservaView.as_view(), name='reserva_proceso'),
]
