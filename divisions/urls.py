from django.urls import path

from . import views

urlpatterns = [
    path('misiones', views.misiones, name='misiones'),
    path('agregar_mision', views.agregar_mision, name='agregar_mision'),
    path('editar_mision/<int:primary_key>', views.editar_mision, name='editar_mision'),
    path('eliminar_mision/<int:primary_key>', views.eliminar_mision, name='eliminar_mision'),

    path('subsistemas', views.subsistemas, name='subsistemas'),
    path('agregar_subsistema', views.agregar_subsistema, name='agregar_subsistema'),
    path('editar_subsistema/<int:primary_key>', views.editar_subsistema, name='editar_subsistema'),
    path('eliminar_subsistema/<int:primary_key>', views.eliminar_subsistema, name='eliminar_subsistema'),
]