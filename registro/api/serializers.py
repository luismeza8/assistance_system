from rest_framework import serializers
from members.models import *
from registro.models import *

from divisions.models import *

class MisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mision
        fields = ('__all__')


class SubsistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsistema
        fields = ('__all__')

class MiembroSerializer(serializers.ModelSerializer):
    misiones = MisionSerializer(many=True, read_only=True)
    subsistemas = SubsistemaSerializer(many=True, read_only=True)

    class Meta:
        model = Miembro
        fields = ('__all__')


class RegistroSerializer(serializers.ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(queryset=Miembro.objects.all())

    class Meta:
        model = Register
        fields = ('__all__')
