from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import *

def registros(request, primary_key):
     registros = Registro.objects.all().filter(miembro=primary_key)
     return render(request, 'registro/registros/registros.html', {'registros': registros})
