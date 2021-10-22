from django.db import models

from Apps.agenda.models import Agenda
from Apps.share.especialidad.models import especialidad
from Apps.usuario.models import usuario

# Create your models here.

class Medico(models.Model):
    id_usuario = models.OneToOneField(
        usuario, models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_agenda = models.ForeignKey(
        Agenda, models.DO_NOTHING, db_column='id_agenda')
    id_especialidad = models.ForeignKey(
        especialidad, models.DO_NOTHING, db_column='id_especialidad')

    class Meta:
        managed = False
        db_table = 'medico'

    # Create /Insert / Add -POST
    # Reatrieve /Fecth -GET
    # Update /Edit - PUT
    # Delete / Remove -DELETE