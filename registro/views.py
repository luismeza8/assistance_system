from django.shortcuts import render 
from django.contrib.auth.decorators import login_required

from .models import *
from members.models import Miembro

@login_required
def registros(request, primary_key, week=None):
    today = timezone.now().date()
    register_this_year = Register.objects.filter(member=primary_key).filter(date__year=today.year).order_by('-date')
    register_in_week = []

    if not week:
        for register in register_this_year:
            if register.date.isocalendar().week == today.isocalendar().week:
                register_in_week.append(register)
    else:
        for register in register_this_year:
            if register.date.isocalendar().week == week:
                register_in_week.append(register)

    miembro = Miembro.objects.get(pk=primary_key)

    if request.htmx:
        template = 'registro/registros/registros.html'
    else:
        template = 'registro/registros/registros_full.html'

    return render(request, template, {'registros': register_in_week, 'miembro': miembro})
