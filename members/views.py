from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse, reverse_lazy
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


class ChangePasswordView(PasswordChangeView):
    success_url = reverse_lazy('miembros')
    template_name = 'members/change_password.html'


@login_required
def change_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password_1', '')
        request.user.set_password(new_password)
        request.user.save()

        return redirect('miembros')

    return render(request, 'members/change_password.html')


def validate_passwords(request):
    response = ''

    old_password = request.POST.get('old_password', False)
    new_password_1 = request.POST.get('new_password_1', False)
    new_password_2 = request.POST.get('new_password_2', False)

    disabled_button = "<button disabled id='btn-submit' class='bg-gray-600 text-secondary px-4 ml-2 rounded-xl hover:shadow-xl'>Cambiar</button>"

    if not request.user.check_password(old_password):
        response += '<p id="old-password-error">La contra no es correcta</p> ' + disabled_button

    if new_password_1 != new_password_2:
        response += '<p id="new-password-error">Las contrasenas no coinciden</p> ' + disabled_button

    if request.user.check_password(old_password) and len(new_password_1) > 1 and new_password_1 == new_password_2:
        response += "<button id='btn-submit' type='submit' class='bg-primary text-secondary px-4 ml-2 rounded-xl hover:shadow-xl'>Cambiar</button>"

    return HttpResponse(response)


@login_required
def access_denied(_):
    return HttpResponse('nop')


@login_required
def view_image(request, image_url):
    context = {
        'image_url': image_url[1:],
    }
    return render(request, 'components/view_image.html', context)


def email_validation(request):
    valid_email = HttpResponse(
        '''
        <button class='bg-primary text-secondary px-4 ml-4 rounded-xl hover:shadow-xl' id="btn-submit">Aceptar</button>"
        '''
    )
    invalid_email = HttpResponse(
        '''
        <p id="email-error">Ya existe un miembro con este correo.</p>
        <button class='bg-grey-800 text-secondary px-4 ml-4 rounded-xl hover:shadow-xl' id="btn-submit" disabled>Aceptar</button>"
        '''
    )
    
    if 'member-id' in request.POST:
        member = Miembro.objects.get(pk=request.POST['member-id'])
        print(f'request {request.POST["email"]}')
        print(f'member {member.email}')
        if request.POST['email'] == member.email:
            return valid_email

    if Miembro.objects.filter(email=request.POST['email']).exists():
        return invalid_email

    return valid_email


@login_required
def miembros(request):
    miembros = Miembro.objects.all()
    template = 'registro/miembros/miembros.html' if request.htmx else 'registro/miembros/miembros_full.html'
    if request.htmx:
        print('yeap')
    
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
            return render(request, 'registro/miembros/formulario_miembro_modal.html', {'form': form, 'url': '/agregar_miembro', 'errores': 'asdf'})
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


