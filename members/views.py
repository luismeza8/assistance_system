from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .decorators import *
from .models import *
from .forms import *

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('miembros')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('miembros')
        else:
            messages.warning(request, 'Error al iniciar sesión.')
            return redirect('login')

    return render(request, 'members/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def access_denied(request):
    return HttpResponse('nop')


@login_required
def miembros(request):
    miembros = Miembro.objects.all()

    if request.htmx:
        template = 'registro/miembros/miembros.html'
    else:
        template = 'registro/miembros/miembros_full.html'
    
    return render(request, template, {'miembros': miembros})


@login_required
@admin_role_required
def agregar_miembro(request):
    if request.method == 'POST':
        form = MiembroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('miembros')
    else:
        form = MiembroForm()
    return render(request, 'registro/miembros/formulario_miembro.html', {'form': form})


@login_required
@admin_role_required
def editar_miembro(request, primary_key):
    miembro = Miembro.objects.get(pk=primary_key)
    form = MiembroForm(instance=miembro)

    if request.method == 'POST':
        form = MiembroForm(request.POST, instance=miembro)
        if form.is_valid():
            form.save()
            return redirect('miembros')

    return render(request, 'registro/miembros/formulario_miembro.html', {'form': form})


@login_required
@admin_role_required
def eliminar_miembro(request, primary_key):
    miembro = Miembro.objects.get(pk=primary_key)
    
    if request.method == 'POST':
        miembro.delete()
        return redirect('miembros')

    return render(request, 'registro/miembros/eliminar_miembro.html', {'miembro': miembro})


@login_required
def misiones(request):
    misiones = Mision.objects.all()

    if request.htmx:
        template = 'registro/misiones/misiones.html'
    else:
        template = 'registro/misiones/misiones_full.html'

    return render(request, template, {'misiones': misiones})


@login_required
@admin_role_required
def agregar_mision(request):
    if request.method == 'POST':
        form = MisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('misiones')
    else:
        form = MisionForm()
    return render(request, 'registro/misiones/formulario_mision.html', {'form': form})


@login_required
@admin_role_required
def editar_mision(request, primary_key):
    mision = Mision.objects.get(pk=primary_key)
    form = MisionForm(instance=mision)

    if request.method == 'POST':
        form = MisionForm(request.POST, instance=mision)
        if form.is_valid():
            form.save()
            return redirect('misiones')
    
    return render(request, 'registro/misiones/formulario_mision.html', {'form': form})


@login_required
@admin_role_required
def eliminar_mision(request, primary_key):
    mision = Mision.objects.get(pk=primary_key)

    if request.method == 'POST':
        mision.delete()
        return redirect('misiones')

    return render(request, 'registro/misiones/eliminar_mision.html', {'mision': mision})


@login_required
def subsistemas(request):
    subsistemas = Subsistema.objects.all()

    if request.htmx:
        template = 'registro/subsistemas/subsistemas.html'
    else:
        template = 'registro/subsistemas/subsistemas_full.html'

    return render(request, template, {'subsistemas': subsistemas})


@login_required
@admin_role_required
def agregar_subsistema(request):
    if request.method == 'POST':
        form = SubsistemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subsistemas')
    else:
        form = SubsistemaForm()
        return render(request, 'registro/subsistemas/formulario_subsistema.html', {'form': form})


@login_required
@admin_role_required
def editar_subsistema(request, primary_key):
    subsistema = Subsistema.objects.get(pk=primary_key)
    form = SubsistemaForm(instance=subsistema)

    if request.method == 'POST':
        form = SubsistemaForm(request.POST, instance=subsistema)
        if form.is_valid():
            form.save()
            return redirect('subsistemas')

    return render(request, 'registro/subsistemas/formulario_subsistema.html', {'form': form})


@login_required
@admin_role_required
def eliminar_subsistema(request, primary_key):
    subsistema = Subsistema.objects.get(pk=primary_key)

    if request.method == 'POST':
        subsistema.delete()
        return redirect('subsistemas')
    return render(request, 'registro/subsistemas/eliminar_subsistema.html', {'subsistema': subsistema})


