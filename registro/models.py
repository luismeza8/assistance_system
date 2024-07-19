from django.db import models
from django.utils import timezone
from members.models import Miembro

import locale

class Register(models.Model):
    member = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, auto_now=False)
    check_in_time = models.TimeField(null=True)
    check_out_time = models.TimeField(null=True)


    def _get_minutes_to_seconds(self, minutes):
        return minutes * 60
    

    def _get_hours_to_seconds(self, hours):
        return hours * 3600


    @property
    def hours_worked(self):
        if self.check_in_time and self.check_out_time:
            check_in_seconds = self.check_in_time.hour * 3600 + self.check_in_time.minute * 60 + self.check_in_time.second
            check_out_seconds = self.check_out_time.hour * 3600 + self.check_out_time.minute * 60 + self.check_out_time.second

            result = check_out_seconds - check_in_seconds

            hours = result / 3600
            minutes = (hours % 1) * 60

            hours = f'0{int(hours)}' if hours < 10 else int(hours) 
            minutes = f'0{int(minutes)}' if minutes < 10 else int(minutes)

            return f'{hours}:{minutes}'
        return '--.--'


    def save(self, *args, **kwargs):
        if self.check_in_time == None:
            self.check_in_time = timezone.now().time()
        else:
            self.check_out_time = timezone.now().time()

        super(Register, self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.member} {self.check_in_time}-{self.check_out_time}'


    # https://pynative.com/python-datetime-format-strftime/
    def get_full_date(self):
        locale.setlocale(locale.LC_ALL, 'es_MX')
        return self.date.strftime('%A %d de %B de %Y')
        
