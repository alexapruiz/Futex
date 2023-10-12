from django import forms
from django.contrib.auth.models import User
from Futex import models


class FormularioTime(forms.ModelForm):
    class Meta:
        model = models.Time
        fields='__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'valor': forms.TextInput(attrs={'class':'form-control'})
        }