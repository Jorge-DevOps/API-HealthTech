from django.db import models
from Apps.share.consultorio.models import Consultorio
from Apps.share.horarioMedico.models import horarioMedico

class Agenda(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    id_horario_medico = models.ForeignKey(
        horarioMedico, models.DO_NOTHING, db_column='id_horario_medico')
    id_consultorio = models.ForeignKey(
        Consultorio, models.DO_NOTHING, db_column='id_consultorio')

    class Meta:
        managed = False
        db_table = 'agenda'

