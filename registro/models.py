from django.db import models
from members.models import Miembro

import locale

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


    # https://pynative.com/python-datetime-format-strftime/
    def get_full_date(self):
        locale.setlocale(locale.LC_ALL, 'es_MX')
        return self.fecha.strftime('%A %d de %B de %Y')
        
