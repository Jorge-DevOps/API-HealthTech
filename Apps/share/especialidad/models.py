from django.db import models

# Create your models here.

class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'especialidad'

