from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class MiembroManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Te falto el email pa')

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


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


class Miembro(AbstractBaseUser, PermissionsMixin):
    ROLES = {
        'M': 'MEMBER',
        'L': 'LEADER',
        'A': 'ADMIN'
    }

    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    mision = models.ManyToManyField(Mision)
    subsistema = models.ManyToManyField(Subsistema)
    horas_acordadas = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(max_length=1, choices=ROLES, default='M')

    objects = MiembroManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.nombre


    def is_leader(self):
        return self.role == self.ROLES['L']


    def is_admin(self):
        return self.role == self.ROLES['A']


    def is_member(self):
        return self.role == self.ROLES['M']

    @property
    def is_staff(self):
        return self.is_admin


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

