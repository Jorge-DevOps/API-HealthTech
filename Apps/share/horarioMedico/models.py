from django.db import models
from . import forms
# Create your models here.

class horarioMedico(models.Model):
    id_horario_medico = models.AutoField(primary_key=True)
    hora_inicio       = models.TimeField()
    hora_fin          = models.TimeField()

    class Meta:
        managed = False
        db_table = 'horario_medico'