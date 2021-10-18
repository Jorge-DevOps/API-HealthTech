from django.db import models

# Create your models here.
class OrdenRemision(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_usuario_paciente = models.ForeignKey(
        'Paciente', models.DO_NOTHING, db_column='id_usuario_paciente')
    id_usuario_medico = models.ForeignKey(
        Medico, models.DO_NOTHING, db_column='id_usuario_medico')
    id_especialidad = models.ForeignKey(
        Especialidad, models.DO_NOTHING, db_column='id_especialidad')

    class Meta:
        managed = False
        db_table = 'orden_remision'


class Paciente(models.Model):
    id_usuario = models.OneToOneField(
        'Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    contrato = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'paciente'


class Medico(models.Model):
    id_usuario = models.OneToOneField(
        'Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_agenda = models.ForeignKey(
        Agenda, models.DO_NOTHING, db_column='id_agenda')
    id_especialidad = models.ForeignKey(
        Especialidad, models.DO_NOTHING, db_column='id_especialidad')

    class Meta:
        managed = False
        db_table = 'medico'


class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'especialidad'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'