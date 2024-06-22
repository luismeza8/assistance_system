from django.shortcuts import render 
from django.contrib.auth.decorators import login_required

from .models import *

@login_required
def registros(request, primary_key):
    registros = Registro.objects.filter(miembro=primary_key).order_by('-fecha')

    if request.htmx:
        template = 'registro/registros/registros.html'
    else:
        template = 'registro/registros/registros_full.html'

    return render(request, template, {'registros': registros})
