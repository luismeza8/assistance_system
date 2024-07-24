from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from members.decorators import *

from .models import *
from .forms import *

# Create your views here.
@login_required
def misiones(request):
    misiones = Mision.objects.all()
    template = 'divisions/misiones/misiones.html' if request.htmx else 'divisions/misiones/misiones_full.html'

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
    return render(request, 'divisions/misiones/formulario_mision_modal.html', {'form': form, 'url': f'agregar_mision'})


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
    
    return render(request, 'divisions/misiones/formulario_mision_modal.html', {'form': form, 'url': f'editar_mision/{primary_key}'})


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
    template = 'divisions/subsistemas/subsistemas.html' if request.htmx else 'divisions/subsistemas/subsistemas_full.html'

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
        return render(request, 'divisions/subsistemas/formulario_subsistema_modal.html', {'form': form, 'url': '/agregar_subsistema'})


@login_required
@admin_role_required
def editar_subsistema(request, primary_key):
    subsistema = Subsistema.objects.get(pk=primary_key)
    form = SubsistemaForm(instance=subsistema)

    if request.method == 'POST':
        form = SubsistemaForm(request.POST, instance=subsistema)
        if form.is_valid():
            form.save()
            messages.success(request, 'yeap')
            return redirect('subsistemas')

    return render(request, 'divisions/subsistemas/formulario_subsistema_modal.html', {'form': form, 'url': f'/editar_subsistema/{primary_key}'})


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


