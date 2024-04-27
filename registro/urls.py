from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('misiones', views.gestionar_misiones, name='misiones'),
]
