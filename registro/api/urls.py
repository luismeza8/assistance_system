from django.urls import path

from . import views

urlpatterns = [
    path('agregar_registro', views.agregar_registro),
]
