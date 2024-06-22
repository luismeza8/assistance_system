from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import timedelta


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

    first_names = models.CharField(max_length=100, default='')
    last_names = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=12, default='')
    email = models.EmailField(max_length=255, unique=True)
    mision = models.ManyToManyField(Mision)
    subsistema = models.ManyToManyField(Subsistema)
    hours_per_week = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(max_length=1, choices=ROLES, default='M')
    profile_picture = models.ImageField(upload_to='users_profile_picture', default='users_profile_picture/default_profile_picture.jpg')
    schedule = models.ImageField(upload_to='schedules', blank=True)

    objects = MiembroManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.first_names} {self.last_names}'


    def get_full_name(self):
        return f'{self.first_names} {self.last_names}'


    def get_name(self):
        first_name = self.first_names.split()[0]
        last_name = self.last_names.split()[0]
        return f'{first_name} {last_name}'


    def is_leader(self):
        return self.role == 'L'


    def is_admin(self):
        return self.role == 'A'


    def is_member(self):
        return self.role == 'M'

    @property
    def is_staff(self):
        return self.is_admin


    def seconds_worked_this_week(self):
        from registro.models import Registro
        hoy = timezone.now().date()
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        fin_semana = inicio_semana + timedelta(days=6)
        registros_semana_actual = Registro.objects.filter(miembro=self).filter(fecha__range=[inicio_semana, fin_semana])

        if len(registros_semana_actual) < 2:
            return 0

        segundos_trabajados = 0

        for i, registro in enumerate(registros_semana_actual):
            if len(registros_semana_actual) > i+1:
                if registro.tipo == 'E' and registros_semana_actual[i+1].tipo == 'S':
                    entrada = registro
                    salida = registros_semana_actual[i+1]
                    diferencia = salida.fecha - entrada.fecha
                    diferencia_en_segundos = diferencia.total_seconds()
                    segundos_trabajados += diferencia_en_segundos

        return segundos_trabajados


    def get_hours_worked_this_week(self):
        seconds = self.seconds_worked_this_week()
        hours = int(seconds // 3600)
        return f'0{hours}' if len(str(hours)) == 1 else hours


    def get_minutes_worked_this_week(self):
        seconds = self.seconds_worked_this_week()
        minutes = int((seconds / 3600) % 1 * 60)
        return f'0{minutes}' if len(str(minutes)) == 1 else minutes


    def get_time_worked_this_week(self):
        return f'{self.get_hours_worked_this_week()}:{self.get_minutes_worked_this_week()}'

