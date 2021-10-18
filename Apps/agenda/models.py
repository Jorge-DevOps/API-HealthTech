from django.db import models
from Apps.share.consultorio.models import consultorio

class Agenda(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    id_horario_medico = models.ForeignKey(
        'HorarioMedico', models.DO_NOTHING, db_column='id_horario_medico')
    id_consultorio = models.ForeignKey(
        consultorio, models.DO_NOTHING, db_column='id_consultorio')

    class Meta:
        managed = False
        db_table = 'agenda'

