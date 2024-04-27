from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

# Create your views here.
def index(request):
    miembros = Miembro.objects.all()
    return render(request, 'registro/inicio.html', {'miembros': miembros})

def gestionar_misiones(request):
    misiones = Mision.objects.all()
    return render(request, 'registro/misiones.html', {'misiones': misiones})
