from django.db import models

from Apps.agenda.models import Agenda
from Apps.share.especialidad.models import especialidad
from Apps.usuario.models import usuario

# Create your models here.
"""Herada de la clase abstrad de Usuario"""
class Medico(usuario):
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