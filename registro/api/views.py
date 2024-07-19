from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from registro.models import *

@api_view(['POST'])
def agregar_registro(request):
    member_id = request.data.get('member')
    member = Miembro.objects.get(pk=member_id)
    last_register = member.register_set.last()

    if last_register.check_in_time == None or last_register.check_out_time != None:
        serializer = RegistroSerializer(data=request.data)
    else:
        serializer = RegistroSerializer(instance=last_register, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)

