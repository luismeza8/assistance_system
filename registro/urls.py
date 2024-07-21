from django.urls import path

from . import views

urlpatterns = [
    path('registros/<int:primary_key>/', views.registros, name='registros'),
    path('registros/<int:primary_key>/<int:number_week>/', views.registros, name='registros'),
]
