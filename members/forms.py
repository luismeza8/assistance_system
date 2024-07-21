from django import forms
from django.urls import reverse_lazy
from .models import *

from divisions.models import *


class MiembroForm(forms.ModelForm):
    first_names = forms.CharField(
        label='first_names',
        widget=forms.TextInput(attrs={'class': 'text-field'})    
    )
    last_names = forms.CharField(
        label='last_names',
        widget=forms.TextInput(attrs={'class': 'text-field'})    
    )
    phone_number = forms.CharField(
        label='phone_number',
        widget=forms.TextInput(attrs={'class': 'text-field'})    
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'text-field',
                'hx-post': reverse_lazy('email_validation'),
                'hx-target': '#email-error',
                'hx-select': '#email-error',
                'hx-select-oob': '#btn-submit',
                'hx-trigger': 'keyup[target.value.length > 3]',
            }
        )
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

    class Meta:
        model = Miembro
        fields = '__all__'
        exclude = ('password',)

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
