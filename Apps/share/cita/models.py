from django.db import models
from Apps.agenda.models import Agenda
from Apps.share.paciente.models import Paciente
from Apps.horario.models import horario
# Create your models here.
class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_agenda = models.ForeignKey(
        Agenda, models.DO_NOTHING, db_column='id_agenda')
    id_usuario = models.ForeignKey(
        Paciente, models.DO_NOTHING, db_column='id_usuario')
    fecha = models.DateField()
    id_horario = models.ForeignKey(
        horario, models.DO_NOTHING, db_column='id_horario')

    class Meta:
        managed = False
        db_table = 'cita'