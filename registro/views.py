from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

# Create your views here.
def index(request):
    miembros = Miembro.objects.all()
    return render(request, 'registro/inicio/index.html', {'miembros': miembros})

def gestionar_misiones(request):
    return HttpResponse('yeap')
