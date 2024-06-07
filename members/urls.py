from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),

    path('miembros', views.miembros, name='miembros'),
    path('agregar_miembro', views.agregar_miembro, name='agregar_miembro'),
    path('editar_miembro/<int:primary_key>', views.editar_miembro, name='editar_miembro'),
    path('eliminar_miembro/<int:primary_key>', views.eliminar_miembro, name='eliminar_miembro'),

    path('misiones', views.misiones, name='misiones'),
    path('agregar_mision', views.agregar_mision, name='agregar_mision'),
    path('editar_mision/<int:primary_key>', views.editar_mision, name='editar_mision'),
    path('eliminar_mision/<int:primary_key>', views.eliminar_mision, name='eliminar_mision'),

    path('subsistemas', views.subsistemas, name='subsistemas'),
    path('agregar_subsistema', views.agregar_subsistema, name='agregar_subsistema'),
    path('editar_subsistema/<int:primary_key>', views.editar_subsistema, name='editar_subsistema'),
    path('eliminar_subsistema/<int:primary_key>', views.eliminar_subsistema, name='eliminar_subsistema'),
]
