from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
class Subsistema(models.Model):
    nombre = models.CharField(max_length=100)
    lider = models.ForeignKey('Miembro', on_delete=models.CASCADE, related_name='lider', null=True, blank=True)

    def __str__(self):
        return self.nombre

#categorias


class Mision(models.Model):
    nombre = models.CharField(max_length=100)
    lider = models.ForeignKey('Miembro', on_delete=models.CASCADE, related_name='lider_de', null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()

    def __str__(self):
        return self.nombre


class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    nfc_id = models.CharField(max_length=100, default='')
    mision = models.ManyToManyField(Mision)
    subsistema = models.ManyToManyField(Subsistema)
    horas_acordadas = models.IntegerField()

    def __str__(self):
        return self.nombre


    def horas_trabajadas_esta_semana(self):
        hoy = timezone.now().date()
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        fin_semana = inicio_semana + timedelta(days=6)
        registros_semana_actual = Registro.objects.filter(miembro=self).filter(fecha__range=[inicio_semana, fin_semana])
        if len(registros_semana_actual) < 2:
            return 0
        segundos_trabajados = 0
        horas_trabajadas = 0

        for i, registro in enumerate(registros_semana_actual):
            if registro.tipo == 'E' and registros_semana_actual[i+1].tipo == 'S':
                entrada = registro
                salida = registros_semana_actual[i+1]
                diferencia = salida.fecha - entrada.fecha
                diferencia_en_segundos = diferencia.total_seconds()
                segundos_trabajados += diferencia_en_segundos

        horas_trabajadas = int(segundos_trabajados // 3600)

        return horas_trabajadas


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
