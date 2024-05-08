from django.urls import path

from . import views

urlpatterns = [
    path('agregar_registro', views.agregar_registro),
    path('obtener_miembro/<int:pk>', views.obtener_miembro),
]
