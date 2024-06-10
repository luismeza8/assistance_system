from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import *

@login_required
def registros(request, primary_key):
    registros = Registro.objects.all().filter(miembro=primary_key)

    if request.htmx:
        template = 'registro/registros/registros.html'
    else:
        template = 'registro/registros/registros_full.html'

    return render(request, template, {'registros': registros})
