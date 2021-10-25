from django.db import models

# Create your models here.

class Consultorio(models.Model):
    id_consultorio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    piso = models.IntegerField()
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'consultorio'