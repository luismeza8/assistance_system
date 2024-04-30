from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import *
from .forms import *

def index(request):
    miembros = Miembro.objects.all()
    return render(request, 'registro/inicio.html', {'miembros': miembros})


def gestionar_misiones(request):
    misiones = Mision.objects.all()
    return render(request, 'registro/misiones.html', {'misiones': misiones})


def agregar_miembro(request):
    if request.method == 'POST':
        form = MiembroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MiembroForm()
    return render(request, 'registro/formulario_miembro.html', {'form': form})


def editar_miembro(request, primary_key):
    miembro = Miembro.objects.get(pk=primary_key)
    form = MiembroForm(instance=miembro)

    if request.method == 'POST':
        form = MiembroForm(request.POST, instance=miembro)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'registro/formulario_miembro.html', {'form': form})


def eliminar_miembro(request, primary_key):
    miembro = Miembro.objects.get(pk=primary_key)
    
    if request.method == 'POST':
        miembro.delete()
        return redirect('index')

    return render(request, 'registro/eliminar_miembro.html', {'miembro': miembro})


def agregar_mision(request):
    if request.method == 'POST':
        form = MisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('misiones')
    else:
        form = MisionForm()
    return render(request, 'registro/formulario_misiones.html', {'form': form})


def editar_mision(request, primary_key):
    mision = Mision.objects.get(pk=primary_key)
    form = MisionForm(instance=mision)

    if request.method == 'POST':
        form = MisionForm(request.POST, instance=mision)
        if form.is_valid():
            form.save()
            return redirect('misiones')
    
    return render(request, 'registro/formulario_misiones.html', {'form': form})


def eliminar_mision(request, primary_key):
    mision = Mision.objects.get(pk=primary_key)

    if request.method == 'POST':
        mision.delete()
        return redirect('misiones')

    return render(request, 'registro/eliminar_mision.html', {'mision': mision})


def subsistemas(request):
    subsistemas = Subsistema.objects.all()
    return render(request, 'registro/subsistemas.html', {'subsistemas': subsistemas})


def agregar_subsistema(request):
    if request.method == 'POST':
        form = SubsistemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subsistemas')
    else:
        form = SubsistemaForm()
        return render(request, 'registro/formulario_subsistema.html', {'form': form})


def editar_subsistema(request, primary_key):
    subsistema = Subsistema.objects.get(pk=primary_key)
    form = SubsistemaForm(instance=subsistema)

    if request.method == 'POST':
        form = SubsistemaForm(request.POST, instance=subsistema)
        if form.is_valid():
            form.save()
            return redirect('subsistemas')

    return render(request, 'registro/formulario_subsistema.html', {'form': form})


def eliminar_subsistema(request, primary_key):
    subsistema = Subsistema.objects.get(pk=primary_key)

    if request.method == 'POST':
        subsistema.delete()
        return redirect('subsistemas')
    return render(request, 'registro/eliminar_subsistema.html', {'subsistema': subsistema})
