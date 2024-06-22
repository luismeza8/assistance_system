from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

from .serializers import *
from registro.models import *

@api_view(['POST'])
def agregar_registro(request):
    serializer = RegistroSerializer(data=request.data)
    if serializer.is_valid():
        try:
            last_register = Registro.objects.filter(miembro=request.data['miembro']).last()
            date_last_register = last_register.fecha.date()
            fecha_actual = datetime.now().date()

            if date_last_register == fecha_actual and last_register.tipo == 'E':
                serializer.validated_data['tipo'] = 'S'
        except:
            pass

        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


@api_view(['GET'])
def obtener_miembro(_, pk):
    miembro = Miembro.objects.get(pk=pk)
    serializer = MiembroSerializer(instance=miembro)
    return Response(serializer.data)
