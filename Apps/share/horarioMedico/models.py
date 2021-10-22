from django.db import models
# Create your models here.

class horarioMedico(models.Model):
    id_horario_medico = models.AutoField(db_column='id_horario_medico', primary_key=True)
    hora_inicio       = models.TimeField(db_column='hora_inicio')
    hora_fin          = models.TimeField(db_column='hora_fin')

    class Meta:
        managed = False
        db_table = 'horario_medico'