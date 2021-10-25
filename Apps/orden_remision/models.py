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

