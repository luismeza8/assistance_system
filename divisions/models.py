from django.db import models


class Subsistema(models.Model):
    nombre = models.CharField(max_length=100)
    lider = models.ForeignKey('members.Miembro', on_delete=models.CASCADE, related_name='lider', null=True, blank=True)


    def __str__(self):
        return str(self.nombre)


class Mision(models.Model):
    nombre = models.CharField(max_length=100)
    lider = models.ForeignKey('members.Miembro', on_delete=models.CASCADE, related_name='lider_de', null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()

    def __str__(self):
        return str(self.nombre)
