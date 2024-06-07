from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from members.models import Miembro

class Registro(models.Model):
    TIPO = {
        'E': 'Entrada', 
        'S': 'Salida',
    }

    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    tipo = models.CharField(max_length=1, choices=TIPO, default='E')

    def __str__(self):
        return f'{self.miembro} {self.tipo} {self.fecha}'
