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
