from django.db import models
from Apps.share.perfil.models import perfil
from Apps.agenda.models import Agenda
from Apps.share.especialidad.models import especialidad
from django import forms

class FormLogin(forms.Form):
    contrasena = forms.CharField(label='Id', max_length=80)
    
    def __str__(self):
        return self.contrasena

# Create your models here.
class LoginModel(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    numero_documento = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=100)
    id_perfil = models.ForeignKey(
        perfil, models.DO_NOTHING, db_column='id_perfil')
    #Medico
    id_agenda = models.ForeignKey(
        Agenda, models.DO_NOTHING, db_column='id_agenda')
    id_especialidad = models.ForeignKey(
        especialidad, models.DO_NOTHING, db_column='id_especialidad')
    #Paciente
    contrato = models.CharField(max_length=100)
    #Administracion
    