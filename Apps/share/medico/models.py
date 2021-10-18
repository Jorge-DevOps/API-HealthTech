from django.db import models
from Apps.agenda.models import Agenda
from Apps.share.especialidad.models import Especialidad


# Create your models here.

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