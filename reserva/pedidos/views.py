from django.shortcuts import render
# importado nuevo
from django.http.response import JsonResponse
from pedidos.models import Aula, Recurso, Profesor, Reserva
from django.views import View
from datetime import datetime, time
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


class AulaView(View):
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            # cuando se recibe un id
            aulas = list(Aula.objects.filter(id=id).values())
            # verifica si obtuvo elementos y prepara la respuesta
            if len(aulas) > 0:
                aula = aulas[0]
                respuesta = {'message': 'success', 'aula': aula}
            else:
                respuesta = {'message': 'Aula no encontrada'}
        else:
            # sin id, se solicita todos los elementos
            aulas = list(Aula.objects.values())
            if len(aulas) > 0:
                respuesta = {'message': 'success', 'aulas': aulas}
            else:
                respuesta = {'message': 'Aulas no encontradas'}
        # envia la respuesta formateada en Json
        return JsonResponse(respuesta)

    def post(self, request):
        # obtengo de request el body y se asigna en jsonDatos (jsDatos)
        jsDatos = json.loads(request.body)
        Aula.objects.create(
            nombre=jsDatos['nombre'], observacion=jsDatos['observacion'])
        respuesta = {'message': "Success"}
        return JsonResponse(respuesta)

    def put(self, request, id=0):
        # obtengo de request el body y se asigna en jsonDatos (jsDatos)
        jsDatos = json.loads(request.body)
        aulas = list(Aula.objects.filter(id=id).values())
        if len(aulas) > 0:
            aula = Aula.objects.get(id=id)
            aula.nombre = jsDatos['nombre']
            aula.observacion = jsDatos['observacion']
            print(aula.nombre, aula.observacion)
            aula.save()
            
            respuesta = {'message': "Success"}
        else:
            respuesta = {'message': 'Aula no encontrada'}
        return JsonResponse(respuesta)

    def delete(self, request, id=0):
        # verifico que exista el id
        aulas = list(Aula.objects.filter(id=id).values())
        if len(aulas) > 0:
            Aula.objects.filter(id=id).delete()
            respuesta = {'message': "Success"}
        else:
            respuesta = {'message': 'Aula no encontrada'}
        return JsonResponse(respuesta)


class RecursoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            # cuando se recibe un id
            recursos = list(Recurso.objects.filter(id=id).values())
            # verifica si obtuvo elementos y prepara la respuesta
            if len(recursos) > 0:
                recurso = recursos[0]
                respuesta = {'message': 'success', 'recurso': recurso}
            else:
                respuesta = {'message': 'Recurso no encontrado'}
        else:
            # sin id, se solicita todos los elementos
            recursos = list(Recurso.objects.values())
            if len(recursos) > 0:
                respuesta = {'message': 'success', 'recurso': recurso}
            else:
                respuesta = {'message': 'Recurso no encontrado'}
        # envia la respuesta formateada en Json
        return JsonResponse(respuesta)

    def post(self, request):
        # obtengo de request el body y se asigna en jsonDatos (jsDatos)
        jsDatos = json.loads(request.body)
        Recurso.objects.create(
            nombre=jsDatos['nombre'], observacion=jsDatos['observacion'])
        respuesta = {'message': "Success"}
        return JsonResponse(respuesta)

    def put(self, request, id=0):
        # obtengo de request el body y se asigna en jsonDatos (jsDatos)
        jsDatos = json.loads(request.body)
        recursos = list(Recurso.objects.filter(id=id).values())
        if len(recursos) > 0:
            recurso = Recurso.objects.get(id=id)
            recurso.nombre = jsDatos['nombre']
            recurso.observacion = jsDatos['observacion']
            recurso.save()
            respuesta = {'message': "Success"}
        else:
            respuesta = {'message': 'Recurso no encontrado'}
        return JsonResponse(respuesta)

    def delete(self, request, id=0):
        # verifico que exista el id
        recursos = list(Recurso.objects.filter(id=id).values())
        if len(recursos) > 0:
            Recurso.objects.filter(id=id).delete()
            respuesta = {'message': "Success"}
        else:
            respuesta = {'message': 'Recurso no encontrado'}
        return JsonResponse(respuesta)


class ProfesorView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            # cuando se recibe un id
            profesores = list(Profesor.objects.filter(id=id).values())
            # verifica si obtuvo elementos y prepara la respuesta
            if len(profesores) > 0:
                profesor = profesores[0]
                respuesta = {'message': 'success', 'profesor': profesor}
            else:
                respuesta = {'message': 'Profesores no encontrados'}
        else:
            # sin id, se solicita todos los elementos
            profesores = list(Profesor.objects.values())
            if len(profesores) > 0:
                respuesta = {'message': 'success', 'profesores': profesores}
            else:
                respuesta = {'message': 'Recurso no encontrado'}
        # envia la respuesta formateada en Json
        return JsonResponse(respuesta)

    def post(self, request):
        # obtengo de request el body y se asigna en jsonDatos (jsDatos)
        jsDatos = json.loads(request.body)
        Profesor.objects.create(apellido=jsDatos['apellido'],
                                nombre=jsDatos['nombre'],
                                observacion=jsDatos['observacion'])
        respuesta = {'message': "Success"}
        return JsonResponse(respuesta)

    def put(self, request, id=0):
        # obtengo de request el body y se asigna en jsonDatos (jsDatos)
        jsDatos = json.loads(request.body)
        profesores = list(Profesor.objects.filter(id=id).values())
        if len(profesores) > 0:
            profesor = Profesor.objects.get(id=id)
            profesor.apellido = jsDatos['apellido']
            profesor.nombre = jsDatos['nombre']
            profesor.observacion = jsDatos['observacion']
            profesor.save()
            respuesta = {'message': "Success"}
        else:
            respuesta = {'message': 'Profesor no encontrado'}
        return JsonResponse(respuesta)

    def delete(self, request, id=0):
        # verifico que exista el id
        profesores = list(Profesor.objects.filter(id=id).values())
        if len(profesores) > 0:
            Profesor.objects.filter(id=id).delete()
            respuesta = {'message': "Success"}
        else:
            respuesta = {'message': 'Profesor no encontrado'}
        return JsonResponse(respuesta)


class ReservaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            # cuando se recibe un id
            reservas = list(Reserva.objects.filter(id=id).values())
            # verifica si obtuvo elementos y prepara la respuesta
            if len(reservas) > 0:
                reserva = reservas[0]
                respuesta = {'message': 'success', 'reserva': reserva}
            else:
                respuesta = {'message': 'Profesores no encontrados'}
        else:
            # sin id, se solicita todos los elementos
            reservas = list(Reserva.objects.values())
            if len(reservas) > 0:
                respuesta = {'message': 'success', 'reservas': reservas}
            else:
                respuesta = {'message': 'Reservas no encontradas'}
        # envia la respuesta formateada en Json
        return JsonResponse(respuesta)

    def post(self, request):
        # obtengo de request el body y se asigna en jsonDatos (jsDatos)
        jsDatos = json.loads(request.body)
        Reserva.objects.create(
            fecha=datetime.strptime(jsDatos['fecha'], "%d/%m/%Y"),
            desde=time.fromisoformat(jsDatos['desde']),
            # %H 00-23, %M  00-59, %S 00-59
            # desde = time.strptime(jsDatos['desde'],"%H:%M:%S"),
            hasta=time.fromisoformat(jsDatos['hasta']),
            # hasta = time.strptime(jsDatos['hasta'],"%H:%M:%S"),
            aula=jsDatos['aula'],
            recurso=jsDatos['recurso'],
            profesor=jsDatos['profesor'])
        respuesta = {'message': "Success"}
        return JsonResponse(respuesta)

    def put(self, request, id=0):
        # obtengo de request el body y se asigna en jsonDatos (jsDatos)
        jsDatos = json.loads(request.body)
        reservas = list(Reserva.objects.filter(id=id).values())
        if len(reservas) > 0:
            reservas = Reserva.objects.get(id=id)
            # reservas.fecha = datetime.fromisoformat(jsDatos['fecha'])
            # %d 01-31, %m  01-12, %y 00-99, %Y año 4 digitos
            reservas.fecha = datetime.strptime(jsDatos['fecha'], "%d/%m/%Y")
            reservas.desde = time.fromisoformat(jsDatos['desde'])
            # %H 00-23, %M  00-59, %S 00-59
            # reservas.desde = time.strptime(jsDatos['desde'],"%H:%M:%S")
            reservas.hasta = time.fromisoformat(jsDatos['hasta'])
            # reservas.hasta = time.strptime(jsDatos['hasta'],"%H:%M:%S")
            reservas.aula = jsDatos['aula']
            reservas.recurso = jsDatos['recurso']
            reservas.profesor = jsDatos['profesor']
            reservas.save()
            respuesta = {'message': "Success"}
        else:
            respuesta = {'message': 'Profesor no encontrado'}
        return JsonResponse(respuesta)

    def delete(self, request, id=0):
        # verifico que exista el id
        reservas = list(Reserva.objects.filter(id=id).values())
        if len(reservas) > 0:
            Reserva.objects.filter(id=id).delete()
            respuesta = {'message': "Success"}
        else:
            respuesta = {'message': 'Reserva no encontrada'}
        return JsonResponse(respuesta)
