from django.db import models

# Create your models here.
class Perfil(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)
    observacion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'perfil'

