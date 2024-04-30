from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('misiones', views.gestionar_misiones, name='misiones'),
    path('agregar_miembro', views.agregar_miembro, name='agregar_miembro'),
    path('editar_miembro/<int:primary_key>', views.editar_miembro, name='editar_miembro'),
    path('eliminar_miembro/<int:primary_key>', views.eliminar_miembro, name='eliminar_miembro'),
    path('agregar_mision', views.agregar_mision, name='agregar_mision'),
    path('editar_mision/<int:primary_key>', views.editar_mision, name='editar_mision'),
    path('eliminar_mision/<int:primary_key>', views.eliminar_mision, name='eliminar_mision'),

    path('subsistemas', views.subsistemas, name='subsistemas'),
    path('agregar_subsistema', views.agregar_subsistema, name='agregar_subsistema'),
]
