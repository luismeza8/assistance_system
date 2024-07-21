from django import forms

from .models import *
from members.models import Miembro


class MisionForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre de la mision',
        widget=forms.TextInput(attrs={'class': 'text-field'})
    )
    lider = forms.ModelChoiceField(
        label='Lider',
        queryset=Miembro.objects.all(),
        required=True,
    )

    lider.widget.attrs.update({'class': 'text-field'})

    class Meta:
        model = Mision
        fields = ['nombre', 'lider', 'fecha_inicio', 'fecha_finalizacion']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_finalizacion': forms.DateInput(attrs={'type': 'date'}),
        }


class SubsistemaForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre del subsistema',
        widget=forms.TextInput(attrs={'class': 'text-field'})
    )
    lider = forms.ModelChoiceField(
        label='Lider',
        queryset=Miembro.objects.all(),
        required=True,
    )

    lider.widget.attrs.update({'class': 'text-field'})

    class Meta:
        model = Subsistema
        fields = ['nombre', 'lider']
