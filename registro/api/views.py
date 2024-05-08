from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

from .serializers import *
from registro.models import *

@api_view(['POST'])
def agregar_registro(request):
    serializer = RegistroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        fecha_registro = datetime.strptime(serializer.data['fecha'], '%Y-%m-%dT%H:%M:%S.%f').date()
        fecha_actual = datetime.now().date()
        
        registros_hoy = Registro.objects.filter(miembro=request.data['miembro']).filter(fecha__date=fecha_actual).order_by('-fecha')

        if len(registros_hoy) > 1 and registros_hoy[1].tipo == 'E':
            registro = Registro.objects.get(pk=serializer.data['id'])
            registro.tipo = 'S'
            registro.save()

            serializer = RegistroSerializer(instance=registro)

        return Response(serializer.data)

    return Response(serializer.errors)


@api_view(['GET'])
def obtener_miembro(request, pk):
    miembro = Miembro.objects.get(pk=pk)
    serializer = MiembroSerializer(instance=miembro)
    return Response(serializer.data)
