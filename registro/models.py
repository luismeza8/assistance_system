from django.db import models
from django.utils import timezone
from members.models import Miembro

import locale

class Register(models.Model):
    member = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, auto_now=False)
    check_in_time = models.TimeField(null=True)
    check_out_time = models.TimeField(null=True)


    def save(self, *args, **kwargs):
        if self.check_in_time == None:
            self.check_in_time = timezone.now().time()
        else:
            self.check_out_time = timezone.now().time()

        super(Register, self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.member}'


    # https://pynative.com/python-datetime-format-strftime/
    def get_full_date(self):
        locale.setlocale(locale.LC_ALL, 'es_MX')
        return self.date.strftime('%A %d de %B de %Y')
        
