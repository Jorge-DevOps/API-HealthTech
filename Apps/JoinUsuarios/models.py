from django.db import models
from Apps.share.perfil.models import perfil
from Apps.agenda.models import Agenda
from Apps.share.especialidad.models import especialidad

# Create your models here.
class JoinTablesmodel(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=10)
    numero_documento = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    sexo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    grupo_sanguineo = models.CharField(max_length=50)
    estrato = models.IntegerField()
    estado_civil = models.CharField(max_length=50)
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
    