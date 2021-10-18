from django.db import models

# Create your models here.
class Paciente(models.Model):
    id_usuario = models.OneToOneField(
        'Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    contrato = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'paciente'

