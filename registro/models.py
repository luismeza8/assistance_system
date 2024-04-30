from django.db import models

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
    mision = models.ManyToManyField(Mision)
    subsistema = models.ManyToManyField(Subsistema)

    def __str__(self):
        return self.nombre


class Registro(models.Model):
    TIPO = {
        'E': 'Entrada', 
        'S': 'Salida',
    }

    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, related_name='miembro_de')
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    tipo = models.CharField(max_length=1, choices=TIPO, default='E')

    def __str__(self):
        return f'{self.miembro} {self.tipo} {self.fecha}'
