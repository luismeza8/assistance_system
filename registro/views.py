from django.shortcuts import render 
from django.contrib.auth.decorators import login_required

from .models import *
from members.models import Miembro

@login_required
def registros(request, primary_key, number_week=None):
    today = timezone.now().date()
    register_this_year = Register.objects.filter(member=primary_key).filter(date__year=today.year).order_by('-date')
    register_in_week = []
    week = today.isocalendar().week if not number_week else number_week

    for register in register_this_year:
        if register.date.isocalendar().week == week:
            register_in_week.append(register)

    hours_worked_in_week = [0, 0, 0, 0, 0, 0, 0]

    for register in register_in_week:
        if register.date.weekday() == 0:
            hours_worked_in_week[0] += register.hours_worked
        elif register.date.weekday() == 1:
            hours_worked_in_week[1] += register.hours_worked
        elif register.date.weekday() == 2:
            hours_worked_in_week[2] += register.hours_worked
        elif register.date.weekday() == 3:
            hours_worked_in_week[3] += register.hours_worked
        elif register.date.weekday() == 4:
            hours_worked_in_week[4] += register.hours_worked
        elif register.date.weekday() == 5:
            hours_worked_in_week[5] += register.hours_worked
        elif register.date.weekday() == 6:
            hours_worked_in_week[6] += register.hours_worked

    miembro = Miembro.objects.get(pk=primary_key)

    if request.htmx:
        template = 'registro/registros/registros.html'
    else:
        template = 'registro/registros/registros_full.html'

    context = {
        'registros': register_in_week,
        'miembro': miembro,
        'hours': hours_worked_in_week
    }

    return render(request, template, context)
