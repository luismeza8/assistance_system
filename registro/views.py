from django.shortcuts import render 
from django.contrib.auth.decorators import login_required

from .models import *
from members.models import Miembro

@login_required
def registros(request, primary_key):
    registros = Register.objects.filter(member=primary_key).order_by('-date')
    miembro = Miembro.objects.get(pk=primary_key)

    if request.htmx:
        template = 'registro/registros/registros.html'
    else:
        template = 'registro/registros/registros_full.html'

    return render(request, template, {'registros': registros, 'miembro': miembro})
