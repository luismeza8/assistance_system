from django.forms.widgets import DateInput

from django import forms
from .models import *


class MiembroForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'text-field'})    
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'text-field'})
    )
    mision = forms.ModelMultipleChoiceField(
        label='Mision/es',
        queryset=Mision.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox_list'}),
        required=False,
    )
    subsistema = forms.ModelMultipleChoiceField(
        label='Subsistema/s',
        queryset=Subsistema.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox_list'}),
        required=False,
    )
    # role = forms.ModelChoiceField(
    #     label='rol',
    #     queryset=list(Miembro.ROLES.values())
    # )
    #
    # role.widget.attrs.update({'class': 'select'})

    class Meta:
        model = Miembro
        fields = ['nombre', 'email', 'mision', 'subsistema', 'horas_acordadas', 'profile_picture', 'role']


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
