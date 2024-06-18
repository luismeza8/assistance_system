from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
import secrets

from .decorators import *
from .models import *
from .forms import *


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
    template = 'registro/miembros/miembros.html' if request.htmx else 'registro/miembros/miembros_full.html'
    
    return render(request, template, {'miembros': miembros})


@login_required
@admin_role_required
def agregar_miembro(request):
    if request.method == 'POST':
        form = MiembroForm(request.POST, request.FILES)
        if form.is_valid():
            password = secrets.token_urlsafe(10)
            form.instance.set_password(password)

            messages.success(request, f'La contraseña de {form.instance.get_name()} es: {password}')

            form.save()
            return redirect('miembros')
        else:
            print(form.errors.as_data())
    else:
        form = MiembroForm()
    return render(request, 'registro/miembros/formulario_miembro_modal.html', {'form': form, 'url': '/agregar_miembro'})


@login_required
@admin_role_required
def editar_miembro(request, primary_key):
    miembro = Miembro.objects.get(pk=primary_key)
    form = MiembroForm(instance=miembro)

    if request.method == 'POST':
        form = MiembroForm(request.POST, request.FILES, instance=miembro)
        if form.is_valid():
            form.save()
            return redirect('miembros')
        else:
            print(form.errors.as_data())

    return render(request, 'registro/miembros/formulario_miembro_modal.html', {'form': form, 'url': f'/editar_miembro/{miembro.pk}'})


@login_required
@admin_role_required
def eliminar_miembro(request, primary_key):
    miembro = Miembro.objects.get(pk=primary_key)
    
    if request.method == 'POST':
        miembro.delete()
        return redirect('miembros')

    title = f'¿Deseas eliminar al miembro {miembro.get_name()}?'
    url = reverse('eliminar_miembro', kwargs={'primary_key': miembro.pk})

    context = {
        'title': title,
        'url': url
    }

    return render(request, 'components/confirmation_modal.html', context)


@login_required
def misiones(request):
    misiones = Mision.objects.all()
    template = 'registro/misiones/misiones.html' if request.htmx else 'registro/misiones/misiones_full.html'

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
    return render(request, 'registro/misiones/formulario_mision_modal.html', {'form': form, 'url': f'agregar_mision'})


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
    
    return render(request, 'registro/misiones/formulario_mision_modal.html', {'form': form, 'url': f'editar_mision/{primary_key}'})


@login_required
@admin_role_required
def eliminar_mision(request, primary_key):
    mision = Mision.objects.get(pk=primary_key)

    if request.method == 'POST':
        mision.delete()
        return redirect('misiones')

    title = f'¿Deseas eliminar la misión {mision.nombre}?'
    url = reverse('eliminar_mision', kwargs={'primary_key': mision.pk})

    context = {
        'title': title,
        'url': url
    }

    return render(request, 'components/confirmation_modal.html', context)


@login_required
def subsistemas(request):
    subsistemas = Subsistema.objects.all()
    template = 'registro/subsistemas/subsistemas.html' if request.htmx else 'registro/subsistemas/subsistemas_full.html'

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
        return render(request, 'registro/subsistemas/formulario_subsistema_modal.html', {'form': form, 'url': '/agregar_subsistema'})


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

    return render(request, 'registro/subsistemas/formulario_subsistema_modal.html', {'form': form, 'url': f'/editar_subsistema/{primary_key}'})


@login_required
@admin_role_required
def eliminar_subsistema(request, primary_key):
    subsistema = Subsistema.objects.get(pk=primary_key)

    if request.method == 'POST':
        subsistema.delete()
        return redirect('subsistemas')

    title = f'¿Deseas eliminar el subsistema {subsistema.nombre}?'
    url = reverse('eliminar_subsistema', kwargs={'primary_key': subsistema.pk})

    context = {
        'title': title,
        'url': url
    }

    return render(request, 'components/confirmation_modal.html', context)


