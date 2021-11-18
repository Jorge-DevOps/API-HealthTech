from django.db import models

from django import forms

# Create your models here.
class LoginMedico(forms.Form):
    tipoPersona = forms.CharField(label='Hora Inicio', max_length=100)
    user = forms.CharField(label='Hora Inicio', max_length=100)
    password = forms.CharField(label='Hora Fin', max_length=100)

    def __str__(self):
        return self.user
