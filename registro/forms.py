from django.forms.widgets import DateInput

from django import forms
from .models import *


class MiembroForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'nombre'})    
    )
    mision = forms.ModelMultipleChoiceField(
        label='Mision/es',
        queryset=Mision.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox_list'}),
        required=True,
    )
    subsistema = forms.ModelMultipleChoiceField(
        label='Subsistema/s',
        queryset=Subsistema.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox_list'}),
        required=True,
    )

    class Meta:
        model = Miembro
        fields = ['nombre', 'mision', 'subsistema']


class MisionForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre de la mision',
        widget=forms.TextInput(attrs={'class': 'nombre'})
    )
    lider = forms.ModelChoiceField(
        label='Lider',
        queryset=Miembro.objects.all(),
        required=True,
    )

    lider.widget.attrs.update({'class': 'select'})

    class Meta:
        model = Mision
        fields = ['nombre', 'lider', 'fecha_inicio', 'fecha_finalizacion']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_finalizacion': forms.DateInput(attrs={'type': 'date'}),
        }
