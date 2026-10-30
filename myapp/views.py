
import json

from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import profile


@method_decorator(csrf_exempt, name='dispatch')
class ProfileView(View):

    # GET: consultar registros
    def get(self, request, pk=None):

        if pk:
            try:
                persona = profile.objects.get(pk=pk)

                return JsonResponse({
                    'id': persona.id,
                    'nombre': persona.nombre,
                    'edad': persona.edad,
                    'correo': persona.correo
                })

            except profile.DoesNotExist:
                return JsonResponse(
                    {'error': 'Perfil no encontrado'},
                    status=404
                )

        personas = list(
            profile.objects.values('id', 'nombre', 'edad', 'correo')
        )

        return JsonResponse(personas, safe=False)

    # POST: crear un registro
    def post(self, request):

        try:
            datos = json.loads(request.body)

            persona = profile.objects.create(
                nombre=datos['nombre'],
                edad=datos['edad'],
                correo=datos['correo']
            )

            return JsonResponse({
                'mensaje': 'Perfil creado correctamente',
                'id': persona.id
            }, status=201)

        except (json.JSONDecodeError, KeyError, TypeError):
            return JsonResponse(
                {'error': 'Datos inválidos o incompletos'},
                status=400
            )

    # PUT: actualizar un registro
    def put(self, request, pk):

        try:
            persona = profile.objects.get(pk=pk)
            datos = json.loads(request.body)

            persona.nombre = datos['nombre']
            persona.edad = datos['edad']
            persona.correo = datos['correo']
            persona.save()

            return JsonResponse({
                'mensaje': 'Perfil actualizado correctamente'
            })

        except profile.DoesNotExist:
            return JsonResponse(
                {'error': 'Perfil no encontrado'},
                status=404
            )

        except (json.JSONDecodeError, KeyError, TypeError):
            return JsonResponse(
                {'error': 'Datos inválidos o incompletos'},
                status=400
            )

    # DELETE: eliminar un registro
    def delete(self, request, pk):

        try:
            persona = profile.objects.get(pk=pk)
            persona.delete()

            return JsonResponse({
                'mensaje': 'Perfil eliminado correctamente'
            })

        except profile.DoesNotExist:
            return JsonResponse(
                {'error': 'Perfil no encontrado'},
                status=404
            )
